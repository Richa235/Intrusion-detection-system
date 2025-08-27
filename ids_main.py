import argparse
import os
from data_processor import DataProcessor
from model_trainer import ModelTrainer
from packet_sniffer import PacketSniffer
from alert_system import AlertSystem

def train_model():
    """Train the IDS model"""
    print("Training IDS model...")
    
    # Initialize components
    processor = DataProcessor()
    trainer = ModelTrainer()
    
    # Load and preprocess data
    # Note: You need to provide your own dataset or use a sample one
    data = processor.load_data('data/sample_data.csv')
    if data is None:
        print("Please provide a dataset in the data folder")
        return
        
    X_train, X_test, y_train, y_test = processor.preprocess_data(data, 'label')
    
    # Train the model
    model = trainer.train(X_train, y_train)
    
    # Evaluate the model
    trainer.evaluate(X_test, y_test)
    
    # Save the model and scaler
    trainer.save_model('models/ids_model.pkl')
    processor.save_scaler('models/scaler.pkl')
    
    print("Model training completed successfully")

def run_ids():
    """Run the IDS in detection mode"""
    print("Starting Intrusion Detection System...")
    
    # Initialize alert system
    alert_system = AlertSystem()
    alert_system.send_alert("IDS started", "INFO")
    
    # Load trained model and scaler
    processor = DataProcessor()
    trainer = ModelTrainer()
    
    try:
        model = trainer.load_model('models/ids_model.pkl')
        scaler = processor.load_scaler('models/scaler.pkl')
    except FileNotFoundError:
        print("Model or scaler not found. Please train the model first.")
        return
        
    # Initialize packet sniffer
    sniffer = PacketSniffer(model, scaler)
    
    # Start sniffing (capture 500 packets as an example)
    sniffer.start_sniffing(count=500)
    
    alert_system.send_alert("IDS stopped", "INFO")
    print("IDS stopped")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Intrusion Detection System')
    parser.add_argument('--train', action='store_true', help='Train the model')
    parser.add_argument('--run', action='store_true', help='Run the IDS')
    
    args = parser.parse_args()
    
    if args.train:
        train_model()
    elif args.run:
        run_ids()
    else:
        print("Please specify either --train to train the model or --run to start the IDS")