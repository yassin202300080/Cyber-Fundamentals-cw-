#Cyber fundementals CW by Yassin Elkholy ID:2023000800

#task 2
import os

def collect_files(path):
    with open("files.log", "w") as f:
        for dirpath, _, files in os.walk(path):
            for file in files:
                if file.endswith((".txt", ".jpg", ".docx")):
                    f.write(os.path.join(dirpath, file) + "\n")

def main():
    path = input("Specify the path to scan: ")
    collect_files(path)

main()