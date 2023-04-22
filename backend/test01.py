from cryptography.hazmat.primitives.asymmetric import rsa, padding, utils
from cryptography.hazmat.primitives import serialization

# Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Commonly used value for public exponent
    key_size=512  # Key size in bits
)

# Serialize private key to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Serialize public key to PEM format
public_pem = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open('private_key.pem', 'wb') as private_file:
    private_file.write(private_pem)

with open('public_key.pem', 'wb') as public_file:
    public_file.write(public_pem)

print(public_pem)