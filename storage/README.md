# Storage Configuration

## MongoDB (Analytics Store)
We use MongoDB to store processed data for the dashboard.

### 1. Start MongoDB
```bash
cd storage
docker-compose up -d
```

### 2. Access Shell
```bash
docker exec -it mongodb mongosh
```

## HDFS (Data Lake)
Assuming Hadoop is installed locally.

### 1. Start HDFS
```bash
start-dfs.sh
```

### 2. Create Directories
```bash
hdfs dfs -mkdir -p /user/smart_meters/raw
hdfs dfs -mkdir -p /user/smart_meters/processed
```

### 3. Upload Data (Manual Batch Ingestion)
```bash
hdfs dfs -put ../data/smart_meters.csv /user/smart_meters/raw/
```
