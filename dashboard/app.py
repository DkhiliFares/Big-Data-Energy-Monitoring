from flask import Flask, render_template, jsonify
# from pymongo import MongoClient
import random
from datetime import datetime

app = Flask(__name__)

# MongoDB Connection (Uncomment to use real DB)
# client = MongoClient('mongodb://localhost:27017/')
# db = client['smart_grid']
# collection = db['meter_readings']

# Shared list of Governorates
GOVERNORATES = [
    "Ariana", "Beja", "Ben Arous", "Bizerte", "Gabes", "Gafsa", 
    "Jendouba", "Kairouan", "Kasserine", "Kebili", "Kef", "Mahdia", 
    "Manouba", "Medenine", "Monastir", "Nabeul", "Sfax", "Sidi Bouzid", 
    "Siliana", "Sousse", "Tataouine", "Tozeur", "Tunis", "Zaghouan"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # Mock data: Return status for ALL 24 governorates
    data = []
    current_time = datetime.now().strftime("%H:%M:%S")
    
    for gov in GOVERNORATES:
        # Simulate power variations
        if gov in ["Tunis", "Sfax", "Sousse"]:
            power = round(random.uniform(5.0, 15.0), 2)
        else:
            power = round(random.uniform(1.0, 6.0), 2)
            
        data.append({
            'timestamp': current_time,
            'region': gov,
            'power_kw': power
        })
    return jsonify(data)

@app.route('/api/stats')
def get_stats():
    # Mock aggregation: Average Power by Region
    # In production: db.meter_readings.aggregate([{"$group": {"_id": "$region", "avg_power": {"$avg": "$power_kw"}}}])
    
    stats = []
    for gov in GOVERNORATES:
        # Simulate different consumption levels
        if gov in ["Tunis", "Sfax", "Sousse"]: # Industrial/High density
            avg_power = random.uniform(8.0, 12.0)
        else:
            avg_power = random.uniform(2.0, 6.0)
            
        stats.append({
            'region': gov,
            'avg_power': round(avg_power, 2)
        })
    
    # Sort by consumption for better visualization
    stats.sort(key=lambda x: x['avg_power'], reverse=True)
    return jsonify(stats)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
