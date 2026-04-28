# GoD_nullX0
Ultimate Bug Hunting Framework v5.5 - Ghost Control Edition
# 🔱 OMNI-GOD v5.5 (Ghost Control Edition)

![License](https://img.shields.io/badge/license-MIT-red) 
![Python](https://img.shields.io/badge/python-3.x-blue)
![Security](https://img.shields.io/badge/target-Bug%20Bounty-orange)

**Omni-God** is a professional-grade reconnaissance framework built for automated bug hunting. It integrates stealth, priority-based scanning, and real-time mobile alerting to give security researchers a competitive edge in fast-moving bug bounty programs.

---

## 🚀 Key Features
* **Ghost Control**: Integrated IP verification to ensure testing remains behind VPN/Tor layers.
* **P1 - P4 Priority Logic**: Automates reconnaissance workflows mapped to industry-standard vulnerability classifications:
    * **P1**: ATO, Auth Bypass, SQLi, RCE.
    * **P2**: IDOR, XSS, Race Conditions, XXE.
    * **P3**: Info Disclosure, BAC, Path Traversal.
    * **P4**: Security Headers, Clickjacking, Cookie issues.
* **Secure Architecture**: Decoupled credential management to prevent API key leakage.
* **Telegram Sentry**: Instant alerts for critical findings via the Telegram Bot API.

## 🛠️ Installation & Usage
Optimized for **Kali Linux**.

```bash
# Clone the repository
git clone [https://github.com/atanupal22256-dot/GoD_nullX0.git](https://github.com/atanupal22256-dot/GoD_nullX0.git)

# Navigate to the tool
cd GoD_nullX0

# Setup local secrets (Never upload this file)
echo 'TELEGRAM_TOKEN = "your_token"' > secrets_config.py
echo 'TELEGRAM_CHAT_ID = "your_id"' >> secrets_config.py

# Run the framework
python3 GoD_nullX0_Core.py
