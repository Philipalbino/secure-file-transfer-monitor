import hashlib
import requests
from logger import log_event

API_KEY = "c492a6977b1be4953ca8267e61d8e2a3e1b04d6bb27c5bf8d33d8303dfffe081"

def get_file_hash(filepath):

    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()


def scan_hash(file_hash):

    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

    headers = {
        "x-apikey": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json()

        malicious = data["data"]["attributes"]["last_analysis_stats"]["malicious"]

        if malicious > 0:
            print("⚠ Malware detected by VirusTotal!")

            log_event(f"ALERT: VirusTotal detected malware (detections: {malicious})")

        else:
            print("File appears clean according to VirusTotal")

    else:
        print("VirusTotal lookup failed")
