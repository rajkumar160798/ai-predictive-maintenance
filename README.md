# AI-Based Predictive Maintenance for Industrial IoT

This project simulates sensor data from industrial equipment and uses a combination of **rule-based** logic and **AI models** (e.g., Facebook Prophet) to detect early signs of failure. The system triggers **Slack and Email alerts**, providing a real-time anomaly monitoring pipeline suitable for cloud-native environments.

> 📌 Designed for smart factories, edge devices, and intelligent MLOps observability.

---

## 📊 Features

- ✅ Sensor Data Simulation (Temperature, Vibration, Pressure)
- 📈 Time Series Forecasting with Facebook Prophet
- 🚨 Anomaly Detection using uncertainty thresholds
- 🔁 Automated Alerts (Slack + Email)
- 📦 Orchestrated with Apache Airflow (optional)
- 📊 Visualization: Sensor Trends + Correlation Analysis

---

## 🏗️ Architecture
[ Sensor Simulation ] → [ Forecast Model (Prophet) ] → [ Anomaly Detector ] → [ Slack/Email Alerts ] → [ DAG Orchestration ]

---

## 🧪 Project Structure

```bash
ai-predictive-maintenance/
├── data/
│   ├── sensor_logs.csv
│   └── anomalies.csv
├── plots/
│   ├── sensor_data_with_anomalies.png
│   └── correlation_matrix.png
├── src/
│   ├── simulator.py
│   ├── anomaly_detector.py
│   ├── alert.py
│   └── run_detection.py
├── visualize_sensor_data.py
└── README.md
```
---
## Setup Instructions

# 1. Clone the repo
```
git clone https://github.com/rajkumar160798/ai-predictive-maintenance.git
cd ai-predictive-maintenance
```

# 2. Install dependencies
```
pip install -r requirements.txt
```

# 3. Run simulator
```
python src/simulator.py
```

# 4. Run anomaly detection and alerts
```
python src/run_detection.py
```

# 5. Optional: Visualize results
```
python visualize_sensor_data.py
```
---

## Alerts

- ✅ **Slack Webhook Integration**  
- ✅ **Email Alerts via SMTP** 

---

## 👨‍💻 Author
**Raj Kumar Myakala**  
AI | Data | Automation | GCP | Python  
[LinkedIn ](https://www.linkedin.com/in/raj-kumar-myakala-927860264/)  
[GitHub ](https://github.com/rajkumar160798)

---

>  If you like this project, consider starring the repo and following my GitHub for more AI/ML innovations!

