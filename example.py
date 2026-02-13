#!/usr/bin/env python3
"""
Example script to run end-to-end wellness detection on a subset of the data.
"""
from wmdetection.data.loader import load_data
from wmdetection.preprocess.preprocess import preprocess_data
from wmdetection.models.trainer import train_model, evaluate_model

def main():
    # Load data
    df = load_data()

    # Take a subset for example
    df_subset = df.head(100)  # First 100 rows

    # Preprocess
    encoded_df, wellness_df = preprocess_data(df_subset)

    # Prepare for training
    target = "18. How often do you feel depressed or down?"
    X = encoded_df.drop(columns=[target])
    y = encoded_df[target]

    # Train
    model, X_train, X_test, y_train, y_test = train_model(X, y, test_size=0.3)

    # Evaluate
    evaluate_model(model, X_test, y_test)

    print("Example run completed.")

if __name__ == "__main__":
    main()