# agent/monitor.py

import time
import json
import os

SURICATA_LOG = "/var/log/suricata/eve.json"

def follow_file(file_path):
    """Like tail -f: yields new lines from file"""
    with open(file_path, "r") as f:
        # Go to the end of file
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.2)
                continue
            yield line.strip()

def read_suricata_logs():
    """Parses eve.json logs and extracts message + src IP"""
    if not os.path.exists(SURICATA_LOG):
        print(f"❌ Suricata log not found: {SURICATA_LOG}")
        return

    print(f"📖 Monitoring Suricata logs from {SURICATA_LOG}")
    for raw_line in follow_file(SURICATA_LOG):
        try:
            log = json.loads(raw_line)
            if log.get("event_type") in ["alert", "http", "ssh"]:
                msg = log.get("alert", {}).get("signature", "")
                src_ip = log.get("src_ip", "unknown")
                full_log = f"{msg} from {src_ip}"
                yield full_log
        except Exception as e:
            continue
