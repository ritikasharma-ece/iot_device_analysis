import pandas as pd
import random
from pathlib import Path

# ----------------------------
# Read Sensor Logs
# ----------------------------

data_dir = Path(__file__).parent.parent / "data"

logs = pd.read_csv(data_dir / "sensor_logs.csv")

failures = []

failure_id = 1

# ----------------------------
# Detect Failures
# ----------------------------

for _, row in logs.iterrows():

    probability = 0

    # High temperature
    if row["temperature"] > 75:
        probability += 0.35

    # Low battery
    if row["battery"] < 20:
        probability += 0.25

    # High CPU
    if row["cpu_usage"] > 90:
        probability += 0.15

    # Weak signal
    if row["rssi"] < -80:
        probability += 0.10

    # Existing error code
    if row["error_code"] != 0:
        probability += 0.25

    # Randomly decide if failure happens
    if random.random() < probability:

        if row["temperature"] > 75:
            failure_type = "Overheating"

        elif row["battery"] < 20:
            failure_type = "Battery Failure"

        elif row["rssi"] < -80:
            failure_type = "Communication Failure"

        else:
            failure_type = "Firmware Crash"

        if probability >= 0.7:
            severity = "Critical"

        elif probability >= 0.4:
            severity = "Major"

        else:
            severity = "Minor"

        downtime = random.randint(10, 240)

        failures.append({

            "failure_id": failure_id,

            "device_id": row["device_id"],

            "timestamp": row["timestamp"],

            "failure_type": failure_type,

            "severity": severity,

            "downtime_minutes": downtime

        })

        failure_id += 1

# ----------------------------
# Save CSV
# ----------------------------

failures_df = pd.DataFrame(failures)

failures_df.to_csv(data_dir / "failures.csv", index=False)

print(failures_df.head())

print()

print("Total Failures:", len(failures_df))