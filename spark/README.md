# Spark Processing

## Prerequisites
- Spark installed (or use `pyspark` if installed via pip)
- Kafka running
- Python dependencies: `pip install kafka-python pyspark`

## Scripts
1. **producer.py**: Reads `../data/smart_meters.csv` and sends records to Kafka `smart-meters` topic.
2. **stream_processing.py**: Reads from Kafka, parses JSON, filters high consumption (alerts), and prints to console.

## Usage

### 1. Run the Producer
```bash
python3 producer.py
```

### 2. Run the Streaming Job
Submit the job to Spark. Ensure you have the Kafka integration jar.

```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 stream_processing.py
```

*Note: Adjust the Spark version in the package name (3.5.0) to match your installed Spark version.*
