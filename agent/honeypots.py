# agent/honeypots.py

import subprocess

def launch_honeypot(ip):
    print(f"🎣 Launching honeypot for {ip}")
    try:
        # Simulate SSH honeypot (can use Cowrie or just netcat for demo)
        subprocess.Popen(["nc", "-lk", "2222"])
        print(f"🟢 Honeypot active on port 2222")
    except Exception as e:
        print(f"⚠️ Failed to start honeypot: {e}")
