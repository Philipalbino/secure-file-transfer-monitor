import datetime
import os

LOG_FILE = "logs/activity.log"

os.makedirs("logs", exist_ok=True)

def log_event(message):
    with open(LOG_FILE,"a") as log:
        log.write(f"{datetime.datetime.now()} - {message}\n")
