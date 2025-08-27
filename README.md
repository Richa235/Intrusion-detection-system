# Intrusion Detection System (IDS)

An Intrusion Detection System that monitors network traffic for suspicious activities and alerts administrators to potential security breaches using machine learning.

## Features

- **Packet Inspection**: Monitors network traffic and inspects packets for malicious patterns
- **Machine Learning Detection**: Uses Random Forest classifier to detect anomalies
- **Real-time Alerting**: Generates alerts when suspicious activity is detected
- **Multiple Alert Channels**: Console, log file, and email notifications
## Project Structure
IDS/
├── data/
│ └── sample_data.csv # Sample dataset for training
├── models/ # Directory for saved models
├── data_processor.py # Data loading and preprocessing
├── model_trainer.py # Machine learning model training
├── packet_sniffer.py # Network packet capture and analysis
├── alert_system.py # Alert generation and notification
├── ids_main.py # Main application entry point
├── requirements.txt # Python dependencies
├── alert_config.json # Alert system configuration
└── README.md # This file

