import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

# ----------------------------
# Read Devices
# ----------------------------

data_dir = Path(__file__).parent.parent / "data"

devices = pd.read_csv(data_dir / "devices.csv")

# ----------------------------
# Simulation Settings
# ----------------------------

start_date = datetime(2026, 1, 1)
num_days = 90

sensor_logs = []

# ----------------------------
# Generate Logs
# ----------------------------

for _, device in devices.iterrows():

    battery = random.randint(90, 100)

    for day in range(num_days):

        for hour in range(24):

            timestamp = start_date + timedelta(days=day, hours=hour)

            if 0 <= hour < 6:
                cpu = random.randint(10, 25)

            elif 6 <= hour < 12:
                cpu = random.randint(30, 55)

            elif 12 <= hour < 18:
                cpu = random.randint(60, 95)

            else:
                cpu = random.randint(25, 60)

            memory = random.randint(20, 90)

            current = round(150 + cpu * 4 + np.random.normal(0, 15), 2)

            voltage = round(np.random.normal(5.0, 0.05), 2)

            temperature = round(
                28 + cpu * 0.35 + np.random.normal(0, 2),
                2
            )

            battery = max(
                battery - random.uniform(0, 0.02),
                0
            )

            rssi = random.randint(-85, -35)

            error = 0

            if temperature > 70:
                error = 1

            sensor_logs.append({

                "device_id": device["device_id"],

                "timestamp": timestamp,

                "temperature": temperature,

                "voltage": voltage,

                "current": current,

                "battery": round(battery,2),

                "cpu_usage": cpu,

                "memory_usage": memory,

                "rssi": rssi,

                "error_code": error

            })

# ----------------------------
# Save CSV
# ----------------------------

logs_df = pd.DataFrame(sensor_logs)

logs_df.to_csv(data_dir / "sensor_logs.csv", index=False)

print(logs_df.head())

print()

print("Rows Generated:", len(logs_df))