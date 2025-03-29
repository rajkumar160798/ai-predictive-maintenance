import csv
import random
from datetime import datetime, timedelta

output_file = "data/sensor_logs.csv"
start_time = datetime.now()

with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "temperature", "vibration", "pressure"])  # ✅ All 3 columns

    for i in range(100):
        timestamp = (start_time + timedelta(minutes=i)).strftime("%Y-%m-%d %H:%M:%S")
        temperature = round(random.uniform(60, 90), 2)
        vibration = round(random.uniform(0.2, 1.0), 2)
        pressure = round(random.uniform(28, 35), 2)

        writer.writerow([timestamp, temperature, vibration, pressure])
print("Sensor   logs   generated   successfully!")
# ✅ Sensor logs generated successfully!
# ✅ CSV file contains 100 rows and 4 columns: timestamp, temperature, vibration, pressure