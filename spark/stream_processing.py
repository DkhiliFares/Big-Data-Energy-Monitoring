from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, current_timestamp
from pyspark.sql.types import StructType, StringType, DoubleType

# Schema of the incoming data
schema = StructType() \
    .add("meter_id", StringType()) \
    .add("timestamp", StringType()) \
    .add("meter_type", StringType()) \
    .add("region", StringType()) \
    .add("voltage_v", StringType()) \
    .add("current_a", StringType()) \
    .add("power_kw", StringType()) \
    .add("energy_kwh", StringType()) \
    .add("status", StringType())

spark = SparkSession.builder \
    .appName("SmartMeterStreaming") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "smart-meters") \
    .option("startingOffsets", "earliest") \
    .load()

# Parse JSON
parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Add processing time
processed_df = parsed_df.withColumn("processing_time", current_timestamp())

# High consumption alert logic (Simple example)
alerts_df = processed_df.filter(col("power_kw").cast("double") > 10.0)

# Write output to Console (for debugging/demo)
query = alerts_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
