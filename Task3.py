#task3 

from cryptography.fernet import Fernet

generated_key = Fernet.generate_key()
fernet = Fernet(generated_key)

filename = input("Enter the filename to encrypt: ")
with open(filename, "rb") as f:
    data = f.read()
    encrypted = fernet.encrypt(data)

with open(filename + ".enc", "wb") as f:
    f.write(encrypted)

print("File encrypted successfully.")