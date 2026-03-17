# Importing packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
import pandas as pd
import base64
import os
import time
from datetime import datetime
from io import StringIO

# Public key
PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAonYdYlCROrQot/dxVxcN
mDIauYe1fE9cIL3Ha/59fkYjBGfkghK+rXkIJhI2BORfcyZP0SWkQwrLSIP9lV7H
2z5kw6XBVEipITVLZAtmK02XzVtI7DvEmtlCLB+5Q0y0UCBArOeebC9hHCzlCQzL
KQ52qCJ5zTXG/1VmeqP+EhtrDWBl5UqSD+uqLot6koBWnYFhK02WW9VbERrnHmg5
COBeuZiyY/JsyyIY6eg76DYqX9FHvCO8PrTH18qkEMzJvlWoNQR2ZzN46H5RoY3k
t8+vYrQFVF8DmRLqyD8J/8yCSu3ifWMBzS0MMVViwFXT+CmgGAKduE/BrPteVhn1
WQIDAQAB
-----END PUBLIC KEY-----"""

public_key = serialization.load_pem_public_key(PUBLIC_KEY.encode())

# Defining encryption function
def encrypt_value(val):
    if not isinstance(val, str) or val.strip() == "":
        return val
    encrypted = public_key.encrypt(
        val.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(encrypted).decode()

# Loading URLs
df = pd.read_csv("links.csv")
df["roster_url"] = df["roster_url"].str.strip()
links = df["roster_url"].tolist()

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
