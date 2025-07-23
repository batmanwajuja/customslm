# utils/linux_cmds.py

import subprocess

def block_ip_ufw(ip):
    print(f"🚫 Blocking {ip} using UFW")
    try:
        subprocess.run(["sudo", "ufw", "deny", "from", ip], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ UFW error: {e}")

def block_ip_iptables(ip):
    print(f"🛑 Blocking {ip} using iptables")
    try:
        subprocess.run([
            "sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ iptables error: {e}")

def unblock_ip_iptables(ip):
    try:
        subprocess.run([
            "sudo", "iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"
        ], check=True)
        print(f"✅ Unblocked {ip} from iptables")
    except subprocess.CalledProcessError:
        print(f"⚠️ Failed to unblock {ip}")
