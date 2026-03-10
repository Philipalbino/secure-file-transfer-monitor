import re

suspicious_domains = [
    ".xyz", ".top", ".ru", ".tk", ".cn"
]

phishing_keywords = [
    "login", "secure", "account", "update", "verify", "bank"
]

def analyze_url(url):

    risk_score = 0
    findings = []

    # Check suspicious domain endings
    for domain in suspicious_domains:
        if domain in url:
            findings.append(f"Suspicious domain extension detected: {domain}")
            risk_score += 30

    # Detect phishing keywords in URL
    for word in phishing_keywords:
        if word in url.lower():
            findings.append(f"Phishing keyword detected in URL: {word}")
            risk_score += 10

    # Detect very long URLs
    if len(url) > 75:
        findings.append("URL length unusually long")
        risk_score += 20

    # Verdict
    if risk_score >= 60:
        verdict = "DANGEROUS"
    elif risk_score >= 30:
        verdict = "SUSPICIOUS"
    else:
        verdict = "SAFE"

    return verdict, risk_score, findings
