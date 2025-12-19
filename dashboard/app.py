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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
