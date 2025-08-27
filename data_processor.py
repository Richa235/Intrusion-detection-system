import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

class DataProcessor:
    def __init__(self):
        self.scaler = StandardScaler()
        
    def load_data(self, file_path):
        """Load dataset from CSV file"""
        try:
            data = pd.read_csv(file_path)
            print(f"Dataset loaded with shape: {data.shape}")
            return data
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return None
            
    def preprocess_data(self, data, target_column):
        """Preprocess the data: split features and target, scale features"""
        if data is None:
            return None, None, None, None
            
        # Separate features and target
        X = data.drop(target_column, axis=1)
        y = data[target_column]
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Scale the features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        return X_train_scaled, X_test_scaled, y_train, y_test
    
    def save_scaler(self, file_path):
        """Save the fitted scaler for later use"""
        joblib.dump(self.scaler, file_path)
        
    def load_scaler(self, file_path):
        """Load a previously saved scaler"""
        self.scaler = joblib.load(file_path)
        return self.scaler