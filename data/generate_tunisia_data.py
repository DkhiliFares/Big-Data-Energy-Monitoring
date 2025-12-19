import csv
import random
from datetime import datetime, timedelta

# List of 24 Governorates in Tunisia
GOVERNORATES = [
    "Ariana", "Beja", "Ben Arous", "Bizerte", "Gabes", "Gafsa", 
    "Jendouba", "Kairouan", "Kasserine", "Kebili", "Kef", "Mahdia", 
    "Manouba", "Medenine", "Monastir", "Nabeul", "Sfax", "Sidi Bouzid", 
    "Siliana", "Sousse", "Tataouine", "Tozeur", "Tunis", "Zaghouan"
]

METER_TYPES = ["Residential", "Commercial", "Industrial"]

def generate_data(num_records=1000):
    data = []
    base_time = datetime(2025, 6, 1, 8, 0, 0)
    
    for i in range(num_records):
        meter_id = f"SM{str(i+1).zfill(4)}"
        # Randomize time within a 24-hour window
        timestamp = base_time + timedelta(minutes=random.randint(0, 1440))
        
        region = random.choice(GOVERNORATES)
        meter_type = random.choice(METER_TYPES)
        
        # Power consumption logic based on type
        if meter_type == "Industrial":
            voltage = random.uniform(230.0, 240.0)
            current = random.uniform(30.0, 100.0)
        elif meter_type == "Commercial":
            voltage = random.uniform(225.0, 235.0)
            current = random.uniform(10.0, 30.0)
        else: # Residential
            voltage = random.uniform(220.0, 230.0)
            current = random.uniform(2.0, 15.0)
            
        power_kw = (voltage * current) / 1000.0
        energy_kwh = power_kw * 0.25 # Assuming 15-min interval roughly
        status = "OK"

        data.append([
            meter_id, 
            timestamp.strftime("%Y-%m-%d %H:%M"), 
            meter_type, 
            region, 
            round(voltage, 1), 
            round(current, 1), 
            round(power_kw, 2), 
            round(energy_kwh, 2), 
            status
        ])
        
    return data

def save_to_csv(data, filename="smart_meters.csv"):
    header = ["meter_id", "timestamp", "meter_type", "region", "voltage_v", "current_a", "power_kw", "energy_kwh", "status"]
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
    print(f"Generated {len(data)} records in {filename}")

if __name__ == "__main__":
    records = generate_data(1000)
    save_to_csv(records, "smart_meters.csv")
