# Corrective Actions Log – EduBand

## Key Issues and Fixes

| **Issue** | **Action Taken** | **Resolved By** | **Date** |
|-----------|------------------|------------------|----------|
| **Sensor data not being recorded properly by the backend** | Fixed data parsing bug in the sensor data ingestion endpoint | Berkay Acar | Apr 18 |
| **PDF reports showing empty data fields** | Added null checks and default values in PDF generation logic | Hasan Berk Demir | Apr 20 |
| **Mobile app crashing after connecting to device via Bluetooth** | Updated Bluetooth library and implemented error handling | Berkay Acar | Apr 22 |
| **Vibration alert not triggering on attention loss** | Adjusted heart rate fluctuation threshold on microcontroller | Beyza Başeğmez | Apr 23 |
| **CORS issue when connecting mobile frontend to Flask API** | Configured Flask-CORS to allow cross-origin requests | Berkay Acar | Apr 25 |
| **Attention score calculations giving incorrect results** | Refined data smoothing and anomaly detection logic | Hasan Berk Demir | Apr 27 |
| **Device failing to detect hand movement during initial calibration** | Tuned motion sensor sensitivity and tested thresholds | Beyza Başeğmez | Apr 28 |
