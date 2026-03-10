import os
import socket
from logger import log_event
from alert_system import send_alert

def analyze_file(filepath):

    filename = os.path.basename(filepath)

    print("Analyzing file:", filename)

    log_event(f"File detected: {filename}")

    # Detect suspicious extensions
    suspicious_extensions = [".exe", ".bat", ".js", ".vbs"]

    for ext in suspicious_extensions:
        if filename.endswith(ext):

            print("⚠ SECURITY ALERT: Suspicious file detected:", filename)

            log_event(f"ALERT: Suspicious file detected {filename}")

            send_alert(f"Suspicious file detected: {filename}")

    # Get system info
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    log_event(f"Source system: {hostname} ({ip_address})")
