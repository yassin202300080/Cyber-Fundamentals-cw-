# decrypt.py
from cryptography.fernet import Fernet

with open("key.bin", "rb") as key_file:
    key = key_file.read()

with open("files.log.enc", "rb") as enc_file:
    decrypted = Fernet(key).decrypt(enc_file.read())

with open("files.log.decrypted", "wb") as f:
    f.write(decrypted)

print("Decrypted to files.log.decrypted")
