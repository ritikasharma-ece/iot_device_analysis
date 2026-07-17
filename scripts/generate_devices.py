from faker import Faker
import pandas as pd
import random
from pathlib import Path

fake = Faker()

devices = []

for i in range(1, 501):
    factory = random.choice([
    "F001",
    "F002",
    "F003",
    "F004",
    "F005"])
    devices.append({
        "device_id": f"D{i:04}",
        "model": random.choice(["ESP32", "STM32", "Arduino Nano", "Raspberry Pi Pico"]),
        "firmware": random.choice(["1.0", "1.1", "1.2", "2.0"]),
        "location": fake.city(),
        
        "installation_date": fake.date_between("-3y", "today"),
        "factory_id":factory})
        

    

# Create DataFrame
df = pd.DataFrame(devices)



from pathlib import Path

output_dir = Path(__file__).parent.parent / "data"
output_dir.mkdir(exist_ok=True)

df.to_csv(output_dir / "devices.csv", index=False)

print(df.head())