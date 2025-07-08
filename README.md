# MDR-Watchdog

Lightweight threat detection for Linux: detects sudo abuse, rogue users, unapproved installs or apps.

## 🚨 What It Detects

- SUDO usage
- User creation (`useradd`, `adduser`)
- Software installs (via `apt`, `pip`, `yum`)
- Launching tools like `nmap`, `wireshark`, `hydra` (customizable)

## ✅ How to Run

1. Download the project
2. Put logs in `logs/` folder
3. Run:

```bash
python src/monitor.py
