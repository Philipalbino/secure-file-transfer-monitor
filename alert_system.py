import smtplib
from email.mime.text import MIMEText
from logger import log_event

ADMIN_EMAIL = "youremail@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "youremail@example.com"
EMAIL_PASS = "YOUR_APP_PASSWORD"

def send_alert(message):

    print("⚠ SECURITY ALERT:", message)

    log_event("ALERT: " + message)

    msg = MIMEText(message)
    msg["Subject"] = "Security Alert - File Monitoring System"
    msg["From"] = EMAIL_USER
    msg["To"] = ADMIN_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, ADMIN_EMAIL, msg.as_string())
        server.quit()

        print("Email alert sent")

    except Exception as e:
        print("Email failed:", e)
