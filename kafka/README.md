# Kafka Setup Guide

## Prerequisites
- Docker
- Docker Compose

## Quick Start
1. Navigate to this directory:
   ```bash
   cd kafka
   ```
2. Start the services:
   ```bash
   docker-compose up -d
   ```
3. Verify containers are running:
   ```bash
   docker ps
   ```

## Management
**Create Topic `smart-meters`:**
```bash
docker exec broker kafka-topics --create --topic smart-meters --bootstrap-server broker:29092 --partitions 1 --replication-factor 1
```

**List Topics:**
```bash
docker exec broker kafka-topics --list --bootstrap-server broker:29092
```

**Consume Topic (for debugging):**
```bash
docker exec broker kafka-console-consumer --topic smart-meters --bootstrap-server broker:29092 --from-beginning
```
