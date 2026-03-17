# Loading libraries
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
import pandas as pd
import base64

# Loading private key (don't hack me!)
with open("/Users/eljahappelson/Desktop/private_key.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# Defining decryption function
def decrypt_value(val):
    try:
        return private_key.decrypt(
            base64.b64decode(val),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()
    except:
        return val

# Loading CSV
df = pd.read_csv("/Users/eljahappelson/Downloads/scraped_data_x.csv")

# Decrypting columns
sensitive_cols = ["Name", "DOB"]
for col in sensitive_cols:
    if col in df.columns:
        print(f"Decrypting column: {col}")
        df[col] = df[col].apply(decrypt_value)
