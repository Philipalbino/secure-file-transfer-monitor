from flask import Flask, render_template

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
