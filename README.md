# Big Data Energy Monitoring Framework

## Overview
A scalable Big Data framework for monitoring, storing, and analyzing electricity consumption from smart meters in near real-time and batch modes.

## Architecture
**Flow:**
`Smart Meters` -> `Kafka` -> `Spark Streaming/Batch` -> `HDFS` / `MongoDB` -> `Dashboard`

**Components:**
- **Smart Meters**: Data generation (simulated)
- **Kafka**: Data ingestion
- **Spark**: Data processing (Streaming & Batch)
- **HDFS**: Raw & Processed data storage
- **MongoDB**: Analytics storage
- **Web Dashboard**: Visualization

## Requirements
To run this project in a Linux environment, ensure you have the following installed:

### System & Tools
- **OS**: Linux (Ubuntu 20.04/22.04 recommended)
- **Java**: OpenJDK 8 or 11 (`sudo apt install openjdk-11-jdk`)
- **Python**: 3.8+ (`sudo apt install python3`)
- **Docker & Docker Compose**: For containerized services (Kafka, MongoDB)

### Big Data Components
- **Apache Kafka**: 3.x (Run via Docker)
- **Apache Spark**: 3.5.x (with Hadoop 3.3.x binaries)
- **Hadoop HDFS**: 3.3.6 (or run in pseudo-distributed mode / Docker)
- **MongoDB**: 6.x (Run via Docker)

## Project Structure
- `data/`: Raw datasets
- `kafka/`: Kafka configuration and setup
- `spark/`: Python scripts for processing
- `storage/`: Configuration for HDFS and MongoDB
- `dashboard/`: Web application source code

## Quick Start
1. **Setup Kafka**: Go to `kafka/` and run `docker-compose up -d`.
2. **Setup Database**: Go to `storage/` and initialize MongoDB.
3. **Run Producer**: Execute the script in `spark/producer.py`.
4. **Run Processing**: Submit Spark jobs from `spark/`.
5. **View Dashboard**: Run the web app in `dashboard/`.
