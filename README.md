# Secure File Transfer Monitoring System

A cybersecurity monitoring system that detects suspicious file uploads and generates alerts.

## Features

- Real-time file monitoring
- Suspicious file extension detection
- Security alert generation
- Activity logging
- Web dashboard for monitoring events

## Technologies Used

- Python
- Flask
- File Monitoring
- Cybersecurity Threat Detection

## How It Works

1. The system monitors the **uploads folder**.
2. When a new file appears, it is analyzed.
3. Suspicious extensions like `.exe`, `.bat`, `.js` trigger alerts.
4. Events are logged in `logs/activity.log`.
5. The dashboard displays security logs.

## Example Alert
