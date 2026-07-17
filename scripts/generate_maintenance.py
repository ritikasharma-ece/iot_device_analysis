import pandas as pd
import random
from pathlib import Path

# ----------------------------
# Read Failures
# ----------------------------

data_dir = Path(__file__).parent.parent / "data"

failures = pd.read_csv(data_dir / "failures.csv")

maintenance = []

maintenance_id = 1

engineers = [
    "Rahul Sharma",
    "Priya Verma",
    "Amit Kumar",
    "Sneha Gupta",
    "Rohit Singh",
    "Neha Sharma",
    "Arjun Mehta",
    "Karan Patel",
    "Anjali Nair",
    "Vikas Rao"
]

# ----------------------------
# Generate Maintenance Records
# ----------------------------

for _, row in failures.iterrows():

    if row["failure_type"] == "Overheating":

        issue = "Cooling System Inspection"

        cost = random.randint(4000,9000)

        repair_hours = random.randint(3,8)

    elif row["failure_type"] == "Battery Failure":

        issue = "Battery Replacement"

        cost = random.randint(2500,6000)

        repair_hours = random.randint(1,3)

    elif row["failure_type"] == "Communication Failure":

        issue = "Antenna Replacement"

        cost = random.randint(1500,4000)

        repair_hours = random.randint(1,2)

    else:

        issue = "Firmware Update"

        cost = random.randint(500,2000)

        repair_hours = random.randint(1,2)

    maintenance.append({

        "maintenance_id": maintenance_id,

        "failure_id": row["failure_id"],

        "device_id": row["device_id"],

        "maintenance_date": row["timestamp"],

        "engineer": random.choice(engineers),

        "issue": issue,

        "repair_cost": cost,

        "repair_time_hours": repair_hours,

        "status": random.choice([
            "Completed",
            "Completed",
            "Completed",
            "In Progress"
        ])

    })

    maintenance_id += 1

# ----------------------------
# Save CSV
# ----------------------------

maintenance_df = pd.DataFrame(maintenance)

maintenance_df.to_csv(data_dir / "maintenance.csv", index=False)

print(maintenance_df.head())

print()

print("Maintenance Records:", len(maintenance_df))