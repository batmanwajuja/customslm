# agent/responder.py

from utils.parser import extract_ip
from agent.honeypots import launch_honeypot
from utils.linux_cmds import block_ip_ufw, block_ip_iptables

# Switch this to "ufw" or "iptables"
FIREWALL_BACKEND = "iptables" or "ufw"

def respond(log, label):
    ip = extract_ip(log) or "unknown"

    if label == "critical":
        if ip != "unknown":
            if FIREWALL_BACKEND == "ufw":
                block_ip_ufw(ip)
            else:
                block_ip_iptables(ip)
        launch_honeypot(ip)
        log_action(log, label, ip)

    elif label == "watch":
        print(f"👀 Watching suspicious activity from {ip}")
        log_action(log, label, ip)

def log_action(log_text, label, ip):
    with open("logs/activity.log", "a") as f:
        f.write(f"{label.upper()} - {ip} - {log_text}\n")
