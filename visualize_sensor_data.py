# 📘 AI Predictive Maintenance: Data Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Read the sensor data
df = pd.read_csv("data/sensor_logs.csv", parse_dates=["timestamp"])

#Read anomalies if available
anomaly_df = None
if os.path.exists("data/anomalies.csv"):
    anomaly_df = pd.read_csv("data/anomalies.csv", parse_dates=["timestamp"])

# Set the style
sns.set(style="whitegrid")
plt.figure(figsize=(14, 6))

# Plot sensor data
plt.plot(df["timestamp"], df["temperature"], label="Temperature", color="orange")
plt.plot(df["timestamp"], df["vibration"], label="Vibration", color="green")
plt.plot(df["timestamp"], df["pressure"], label="Pressure", color="blue")

# Plot anomalies if available
if anomaly_df is not None and not anomaly_df.empty:
    plt.scatter(anomaly_df["timestamp"], anomaly_df["temperature"], color="red", label="Anomalies", zorder=5)

plt.xlabel("Timestamp")
plt.ylabel("Sensor Values")
plt.title("Simulated Sensor Data with Anomaly Highlights")
plt.legend()
plt.tight_layout()
plt.savefig("plots/sensor_data_with_anomalies.png")  
plt.show()

# === Optional: Correlation Matrix ===
plt.figure(figsize=(6, 4))
corr = df[["temperature", "vibration", "pressure"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("plots/correlation_matrix.png")  
plt.show()
# 📘 AI Predictive Maintenance: Data Visualization

