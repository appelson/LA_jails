from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
import pandas as pd
import base64
import os
import time
from datetime import datetime
from io import StringIO

KEY = bytes.fromhex(os.getenv("AES_KEY"))

def encrypt_value(val):
    if not isinstance(val, str) or val.strip() == "":
        return val
    p = sym_padding.PKCS7(128).padder()
    padded = p.update(val.strip().lower().encode()) + p.finalize()
    cipher = Cipher(algorithms.AES(KEY), modes.ECB())
    e = cipher.encryptor()
    return base64.b64encode(e.update(padded) + e.finalize()).decode()

# Loading URLs
df = pd.read_csv("links.csv")
df["roster_url"] = df["roster_url"].str.strip()
links = df["roster_url"].tolist()[1:2]

os.makedirs("downloads", exist_ok=True)

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/google-chrome-stable"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)
all_dfs = []

for url in links:
    jail = df[df["roster_url"] == url]["parish_jails"].tolist()[0]
    try:
        driver.get(url)
        try:
            show_all = wait.until(EC.element_to_be_clickable((By.ID, "lbShowAll")))
            show_all.click()
            time.sleep(5)
        except Exception:
            pass
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find("table", id="gvRoster")
        if table:
            df_table = pd.read_html(StringIO(str(table)))[0]
            df_table["jail"] = jail
            df_table["url"] = url
            df_table["scraped_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            all_dfs.append(df_table)
            print(f"Scraped: {url}")
        else:
            print(f"No table found: {url}")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

driver.quit()

if all_dfs:
    final_df = pd.concat(all_dfs, ignore_index=True)
    sensitive_cols = ["Name", "DOB"]
    for col in sensitive_cols:
        if col in final_df.columns:
            print(f"Encrypting column: {col}")
            final_df[col] = final_df[col].apply(encrypt_value)
    filename = f"downloads/scraped_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    final_df.to_csv(filename, index=False)
    print(f"Saved to {filename}")
else:
    print("No data scraped.")
