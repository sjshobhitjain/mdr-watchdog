from rules import detect_sudo, detect_user_creation, detect_install_command
import json

def load_approved_apps(path="config/approved_apps.json"):
    with open(path) as f:
        return json.load(f)

def monitor_log(filepath):
    alerts = []
    approved_apps = load_approved_apps()

    with open(filepath) as f:
        for line in f:
            if detect_sudo(line):
                alerts.append(f"[SUDO] {line.strip()}")
            if detect_user_creation(line):
                alerts.append(f"[USER-CREATION] {line.strip()}")
            if detect_install_command(line):
                alerts.append(f"[INSTALL] {line.strip()}")
            for app in approved_apps:
                if app in line:
                    break
            else:
                if "COMMAND=" in line:
                    alerts.append(f"[UNAPPROVED-APP] {line.strip()}")

    return alerts

if __name__ == "__main__":
    alerts = monitor_log("logs/sample_auth.log")
    for alert in alerts:
        print("⚠️", alert)
