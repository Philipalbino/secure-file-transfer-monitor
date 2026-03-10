import re

phishing_keywords = [
    "urgent",
    "verify your account",
    "password reset",
    "click here",
    "login now",
    "suspend your account"
]

suspicious_domains = [
    ".xyz",
    ".top",
    ".ru",
    ".tk"
]

def analyze_email(email_text):

    risk_score = 0
    findings = []

    # Detect phishing keywords
    for keyword in phishing_keywords:
        if keyword.lower() in email_text.lower():
            findings.append(f"Phishing keyword detected: {keyword}")
            risk_score += 20

    # Detect URLs
    urls = re.findall(r'https?://\S+', email_text)

    for url in urls:
        findings.append(f"URL detected: {url}")

        for domain in suspicious_domains:
            if domain in url:
                findings.append(f"Suspicious domain detected: {domain}")
                risk_score += 30

    # Determine risk level
    if risk_score >= 60:
        verdict = "DANGEROUS"
    elif risk_score >= 30:
        verdict = "SUSPICIOUS"
    else:
        verdict = "SAFE"

    return verdict, risk_score, findings
