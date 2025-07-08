import re

def detect_sudo(log_line):
    return "sudo:" in log_line.lower()

def detect_user_creation(log_line):
    return "useradd" in log_line or "adduser" in log_line

def detect_install_command(log_line):
    return any(cmd in log_line for cmd in ["apt install", "yum install", "pip install"])

def detect_unapproved_apps(log_line, approved_apps):
    return any(app in log_line for app in approved_apps) is False
