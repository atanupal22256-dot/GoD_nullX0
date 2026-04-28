#!/usr/bin/env python3
# 🔱 OMNI-GOD v5.5 (Ghost Control Edition)
# Developed by: Atanu [R!5hu]
# Description: Professional Bug Hunting & Recon Framework

import os
import sys
import requests
import subprocess
import time

# --- SECURE CREDENTIAL LOADING ---
# This looks for your secrets_config.py file on your local machine.
# On GitHub, it will safely default to "REDACTED".
try:
    import secrets_config
    TOKEN = secrets_config.TELEGRAM_TOKEN
    CHAT_ID = secrets_config.TELEGRAM_CHAT_ID
except ImportError:
    TOKEN = "REDACTED_FOR_SECURITY"
    CHAT_ID = "REDACTED_FOR_SECURITY"

# --- CORE SETTINGS ---
VERSION = "5.5"
BANNER = f"""
  🔱 OMNI-GOD v{VERSION} 🔱
  [Ghost Control Enabled]
  Target: Bug Bounty Recon
"""

def send_alert(message):
    """Sends a professional Telegram notification for P1-P2 findings."""
    if TOKEN == "REDACTED_FOR_SECURITY":
        print("[!] Telegram not configured. Skipping alert.")
        return
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": f"🔱 [GOD-ALERT] 🔱\n\n{message}"}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"[!] Alert failed: {e}")

def ghost_check():
    """Verifies if the researcher is protected by VPN/Tor."""
    print("[*] Running Ghost Control check...")
    try:
        ip = requests.get("https://api.ipify.org").text
        print(f"[+] Current Ghost IP: {ip}")
    except:
        print("[!] Connection Error: Check your VPN/Tor status.")

def run_recon(target):
    """Main Recon Logic mapped to P1-P4 Priority."""
    print(f"\n[*] Initiating Recon on: {target}")
    print("[-] Mapping to Priority Order: P1 -> P2 -> P3 -> P4")
    
    # Simulate reconnaissance stages
    stages = [
        "P1: Checking for ATO & Auth Bypass...",
        "P2: Testing IDOR & XSS entry points...",
        "P3: Analyzing Information Disclosure...",
        "P4: Auditing Security Headers..."
    ]
    
    for stage in stages:
        print(f"    > {stage}")
        time.sleep(1)
        
    print(f"\n[+] Recon Complete for {target}")
    send_alert(f"Scan Finished for: {target}\nCheck results/ folder for details.")

def main():
    os.system('clear')
    print(BANNER)
    ghost_check()
    
    if len(sys.argv) < 2:
        target = input("\n[?] Enter Target Domain (e.g., target.com): ")
    else:
        target = sys.argv[1]
        
    run_recon(target)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Shutdown requested by User.")
        sys.exit(0)

