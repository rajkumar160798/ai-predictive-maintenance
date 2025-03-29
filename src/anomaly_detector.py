import pandas as pd
from datetime import datetime
from alert import send_slack_alert, send_email_alert

# === Parameters ===
SENSOR_FILE = 'data/sensor_logs.csv'
ANOMALY_FILE = 'data/anomalies.csv'
TEMP_THRESHOLD = 78.0  # Fahrenheit
VIB_THRESHOLD = 2.0    # example threshold for vibration

# === Load sensor data ===
df = pd.read_csv(SENSOR_FILE, parse_dates=['timestamp'])

# === Rule-based anomaly detection ===
anomalies = df[(df['temperature'] > TEMP_THRESHOLD) | (df['vibration'] > VIB_THRESHOLD)]

# === Save anomalies ===
if not anomalies.empty:
    anomalies.to_csv(ANOMALY_FILE, index=False)
    
    # === Format alert message ===
    latest = anomalies.iloc[-1]
    message = (
        f"🚨 Anomaly Detected!\n\n"
        f"Time: {latest['timestamp']}\n"
        f"Temperature: {latest['temperature']}°F\n"
        f"Vibration: {latest['vibration']}g\n"
        f"Pressure: {latest['pressure']} psi\n"
    )

    # === Trigger Alerts ===
    send_slack_alert(message)
    send_email_alert("Anomaly Detected in Sensor Data", message)

    print("[✔] Anomalies found and alerts sent.")
else:
    print("[✓] No anomalies detected.")

def detect_anomalies(file_path):
    import pandas as pd
    from alert import send_slack_alert, send_email_alert

    df = pd.read_csv(file_path)
    latest = df.iloc[-1]
    anomalies = []

    if latest["temperature"] > 78:
        anomalies.append("Temperature")
    if latest["vibration"] > 0.9:
        anomalies.append("Vibration")
    if latest["pressure"] > 34:
        anomalies.append("Pressure")

    if anomalies:
        msg = (
            f"⚠️ Anomaly Detected:\n"
            f"Timestamp: {latest['timestamp']}\n"
            f"Temperature: {latest['temperature']} °F\n"
            f"Vibration: {latest['vibration']} mm/s\n"
            f"Pressure: {latest['pressure']} psi\n"
            f"Issues: {', '.join(anomalies)}"
        )
        send_slack_alert(msg)
        send_email_alert("Anomaly Alert - Sensor Data", msg)

    return pd.DataFrame([latest]) if anomalies else pd.DataFrame()
