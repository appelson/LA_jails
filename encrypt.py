# Importing libraries
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generating private key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Saving private key
with open("/Users/eljahappelson/Desktop/private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption()
    ))

# Saving public key
with open("/Users/eljahappelson/Desktop/public_key.pem", "wb") as f:
    f.write(private_key.public_key().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo
    ))

