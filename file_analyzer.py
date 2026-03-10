import socket
import os
from virustotal_scan import get_file_hash, scan_hash
from logger import log_event
def analyze_file(filepath):

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

log_event(f"Source system: {hostname} ({ip_address})")

    filename = os.path.basename(filepath)

    print("Analyzing file:", filename)

    log_event(f"File detected: {filename}")

    suspicious_extensions = [".exe", ".bat", ".js", ".vbs"]

    for ext in suspicious_extensions:
        if filename.endswith(ext):

            print("⚠ SECURITY ALERT: Suspicious file detected:", filename)

            log_event(f"ALERT: Suspicious file detected {filename}")

    # SHA256 hash
    file_hash = get_file_hash(filepath)

    print("SHA256:", file_hash)

    # VirusTotal scan
    scan_hash(file_hash)
