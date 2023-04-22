from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
import hashlib

# Decrypt ciphertext
ciphertext = "bpGxS/km18sd80epB5jRRw=="  # Replace with the ciphertext generated from JavaScript
key = b"NMSL777"  # 256-bit key
iv = b"This is an IVVV."  # IV (Initialization Vector)

data = b"Hello, world!"  # Data to hash

# Create a SHA-256 hash object
sha256 = hashlib.sha256()

# Update the hash object with the data
sha256.update(key)

# Compute the hash and convert it to hexadecimal
key = sha256.digest()


# Decode base64-encoded ciphertext
ciphertext = b64decode(ciphertext)

# Create an AES cipher object in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt ciphertext
decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)