import requests
import smtplib
from email.mime.text import MIMEText

# === Slack Webhook URL ===
SLACK_WEBHOOK = "https://hooks.slack.com/services/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"

# === Email SMTP Settings ===
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "rk9618289692@gmail.com"
EMAIL_PASS = "**** **** ****"
EMAIL_TO = "myakalarajkumar1998@gmail.com"

def send_slack_alert(message):
    payload = {"text": message}
    try:
        response = requests.post(SLACK_WEBHOOK, json=payload)
        response.raise_for_status()
        print("[Slack] Alert sent.")
    except Exception as e:
        print("[Slack] Failed to send alert:", e)

def send_email_alert(subject, message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_TO

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

        print("[Email] Alert sent.")
    except Exception as e:
        print("[Email] Failed to send alert:", e)
