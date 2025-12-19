from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

def main():
    spark = SparkSession.builder \
        .appName("SmartMeterBatchAnalytics") \
        .getOrCreate()

    # In a real scenario, read from HDFS directory where streaming job dumped data
    # For now, we read the source CSV to demonstrate batch aggregation
    input_path = "../data/smart_meters.csv"

    df = spark.read.option("header", "true").option("inferSchema", "true").csv(input_path)

    print("Calculaing average power consumption by Region...")
    avg_power = df.groupBy("region").agg(
        avg("power_kw").alias("avg_power"),
        count("meter_id").alias("record_count")
    )

    avg_power.show()
    
    # Save results (e.g., to JSON for dashboard to pick up, or back to DB)
    # avg_power.write.format("json").save("output/avg_power_by_region")

    spark.stop()

if __name__ == "__main__":
    main()
