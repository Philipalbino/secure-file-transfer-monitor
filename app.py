from flask import Flask, render_template
from email_analyzer import analyze_email
from flask import request
from url_analyzer import analyze_url
from ai_phishing_detector import predict_email
app = Flask(__name__)

LOG_FILE = "logs/activity.log"

@app.route("/")
def dashboard():

    with open(LOG_FILE, "r") as f:
        logs = f.readlines()

    logs.reverse()

    total_uploads = 0
    total_alerts = 0
    malware_files = 0

    for log in logs:
        if "New file uploaded" in log:
            total_uploads += 1
        if "ALERT" in log:
            total_alerts += 1
            malware_files += 1

    return render_template(
        "dashboard.html",
        logs=logs,
        uploads=total_uploads,
        alerts=total_alerts,
        malware=malware_files
    )

@app.route("/email", methods=["GET", "POST"])
def email_check():

    result = None
    score = None
    findings = []

    if request.method == "POST":
        email_text = request.form["email"]

        result, score, findings = analyze_email(email_text)

    return render_template(
        "email_analyzer.html",
        result=result,
        score=score,
        findings=findings
    )

@app.route("/url", methods=["GET", "POST"])
def url_check():

    result = None
    score = None
    findings = []

    if request.method == "POST":
        url = request.form["url"]

        result, score, findings = analyze_url(url)

    return render_template(
        "url_analyzer.html",
        result=result,
        score=score,
        findings=findings
    )

@app.route("/ai-email", methods=["GET", "POST"])
def ai_email():

    result = None

    if request.method == "POST":
        email_text = request.form["email"]

        result = predict_email(email_text)

    return render_template(
        "ai_email.html",
        result=result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
