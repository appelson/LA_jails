from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
import pandas as pd
import base64
import os
from dotenv import load_dotenv

load_dotenv()
KEY = bytes.fromhex(os.getenv("AES_KEY"))

def decrypt_value(val):
    if not isinstance(val, str) or val.strip() == "":
        return val
    cipher = Cipher(algorithms.AES(KEY), modes.ECB())
    d = cipher.decryptor()
    raw = d.update(base64.b64decode(val)) + d.finalize()
    u = sym_padding.PKCS7(128).unpadder()
    return (u.update(raw) + u.finalize()).decode()

df = pd.read_csv("downloads/FILE.csv")
df["Name"] = df["Name"].apply(decrypt_value)
df["DOB"] = df["DOB"].apply(decrypt_value)
print(df.head())
