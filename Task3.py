#task3

from cryptography.fernet import Fernet
import os
generated_key = Fernet.generate_key()
with open("key.bin", "wb") as key_file:
    key_file.write(generated_key)

fernet = Fernet(generated_key)

#Encrypt files.log
with open("files.log", "rb") as f:
    data = f.read()
    encrypted = fernet.encrypt(data)

with open("files.log.enc", "wb") as f:
    f.write(encrypted)

print("File encrypted successfully.")