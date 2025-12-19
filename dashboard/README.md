# Dashboard

Simple Flask Web App to visualize Smart Meter data.

## Prerequisites
- Python 3.x
- Flask: `pip install flask`

## Running
1. Navigate to dashboard directory:
   ```bash
   cd dashboard
   ```
2. Run the app:
   ```bash
   python3 app.py
   ```
3. Open browser at `http://localhost:5000`

## Configuration
- Modify `app.py` to uncomment the MongoDB connection lines when you have real data flowing into MongoDB from the Spark Batch/Streaming jobs.
