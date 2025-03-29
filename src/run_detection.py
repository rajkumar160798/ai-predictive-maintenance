# src/run_detection.py

from anomaly_detector import detect_anomalies
from alert import send_slack_alert

detect_anomalies("data/sensor_logs.csv")
send_slack_alert("Anomaly detected in sensor data.")

# Path to CSV data
csv_file = 'data/sensor_logs.csv'

# Path to save anomaly results
output_file = 'data/anomalies.csv'

# Slack webhook
webhook_url = "https://hooks.slack.com/services/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"

# Run anomaly detection
anomalies = detect_anomalies(csv_file)


# If anomalies found, send alert
if not anomalies.empty:
    message = f"⚠️ {len(anomalies)} anomalies detected in sensor data.\nCheck: {output_file}"
    send_slack_alert(message, webhook_url)
    print("Alert sent!")
else:
    print("✅ No anomalies found.")
