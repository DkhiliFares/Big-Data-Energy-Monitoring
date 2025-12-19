import time
import csv
import json
from kafka import KafkaProducer
import sys

# Configuration
KAFKA_BROKER = 'localhost:9092'
TOPIC = 'smart-meters'
DATA_FILE = '../data/smart_meters.csv'

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

def main():
    try:
        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_BROKER],
            value_serializer=json_serializer
        )
        print(f"Connected to Kafka at {KAFKA_BROKER}")
    except Exception as e:
        print(f"Error connecting to Kafka: {e}")
        return

    print(f"Reading from {DATA_FILE}...")
    
    with open(DATA_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Simulate real-time by adding current timestamp or keeping original if simulating past
            # Sending data
            print(f"Sending: {row['meter_id']}")
            producer.send(TOPIC, row)
            time.sleep(1) # Simulate delay

    producer.flush()
    print("Done producing data.")

if __name__ == "__main__":
    main()
