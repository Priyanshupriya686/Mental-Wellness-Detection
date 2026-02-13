#!/usr/bin/env python3
"""
CLI for training the model.
"""
import argparse
from wmdetection.data.loader import load_data
from wmdetection.preprocess.preprocess import preprocess_data
from wmdetection.models.trainer import train_model, evaluate_model

def main():
    parser = argparse.ArgumentParser(description="Train the wellness detection model.")
    parser.add_argument("--data-path", type=str, help="Path to the data CSV file.")
    args = parser.parse_args()

    # Load data
    df = load_data(args.data_path)

    # Preprocess
    encoded_df, wellness_df = preprocess_data(df)

    # Prepare for training
    target = "18. How often do you feel depressed or down?"
    X = encoded_df.drop(columns=[target])
    y = encoded_df[target]

    # Train
    model, X_train, X_test, y_train, y_test = train_model(X, y)

    # Evaluate
    evaluate_model(model, X_test, y_test)

    print("Model trained successfully.")

if __name__ == "__main__":
    main()