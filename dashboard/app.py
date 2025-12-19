from flask import Flask, render_template, jsonify
# from pymongo import MongoClient
import random
from datetime import datetime

app = Flask(__name__)

# MongoDB Connection (Uncomment to use real DB)
# client = MongoClient('mongodb://localhost:27017/')
# db = client['smart_grid']
# collection = db['meter_readings']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # Mock data for demonstration if DB is empty or not connected
    # In production, query MongoDB: list(collection.find().limit(50))
    data = []
    regions = ['Tunis', 'Ariana', 'Ben Arous', 'Sfax', 'Bizerte']
    current_time = datetime.now().strftime("%H:%M:%S")
    
    for i in range(5):
        data.append({
            'timestamp': current_time,
            'region': regions[i],
            'power_kw': round(random.uniform(1.0, 15.0), 2)
        })
    return jsonify(data)

@app.route('/api/stats')
def get_stats():
    # Mock aggregation: Average Power by Region
    # In production: db.meter_readings.aggregate([{"$group": {"_id": "$region", "avg_power": {"$avg": "$power_kw"}}}])
    
    # Using the 24 governorates list for demo
    governorates = [
        "Ariana", "Beja", "Ben Arous", "Bizerte", "Gabes", "Gafsa", 
        "Jendouba", "Kairouan", "Kasserine", "Kebili", "Kef", "Mahdia", 
        "Manouba", "Medenine", "Monastir", "Nabeul", "Sfax", "Sidi Bouzid", 
        "Siliana", "Sousse", "Tataouine", "Tozeur", "Tunis", "Zaghouan"
    ]
    
    stats = []
    for gov in governorates:
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
