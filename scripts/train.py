#!/usr/bin/env python3
"""
Training script for Mental Wellness Detection model.

This script trains a machine learning model on the social media mental health dataset
and saves the trained model along with training metrics.
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

# Import our preprocessing utilities
from preprocess import preprocess_data


def load_social_media_mental_health(data_path=None):
    """
    Load the social media mental health dataset.

    Args:
        data_path: Path to the CSV file. If None, uses default path.

    Returns:
        pd.DataFrame: Loaded dataset
    """
    if data_path is None:
        # Default path
        data_path = "Datasets/Social media & Mental Health/smmh.csv"

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found at {data_path}")

    df = pd.read_csv(data_path)
    print("✅ Loaded dataset")
    print("Shape:", df.shape)
    return df


def train_model(X_train, y_train, model_params):
    """
    Train the RandomForest model with given parameters.

    Args:
        X_train: Training features
        y_train: Training labels
        model_params: Dictionary of model parameters

    Returns:
        Trained model
    """
    model = RandomForestClassifier(**model_params)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model and return metrics.

    Args:
        model: Trained model
        X_test: Test features
        y_test: Test labels

    Returns:
        Dictionary containing evaluation metrics
    """
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    # Classification report as dict
    class_report = classification_report(y_test, y_pred, output_dict=True)

    # Confusion matrix as list for JSON serialization
    conf_matrix = confusion_matrix(y_test, y_pred).tolist()

    metrics = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'classification_report': class_report,
        'confusion_matrix': conf_matrix,
        'test_samples': len(y_test)
    }

    return metrics


def save_model_and_metrics(model, metrics, model_path, metrics_path):
    """
    Save the trained model and metrics to disk.

    Args:
        model: Trained model
        metrics: Evaluation metrics
        model_path: Path to save model
        metrics_path: Path to save metrics
    """
    # Create directories if they don't exist
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    os.makedirs(os.path.dirname(metrics_path), exist_ok=True)

    # Save model
    joblib.dump(model, model_path)
    print(f" Model saved to: {model_path}")

    # Save metrics
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=2)
    print(f" Metrics saved to: {metrics_path}")


def main():
    parser = argparse.ArgumentParser(description='Train Mental Wellness Detection Model')

    # Data arguments
    parser.add_argument('--data-path', type=str, default=None,
                       help='Path to data file (default: use built-in data loader)')

    # Model arguments
    parser.add_argument('--n-estimators', type=int, default=100,
                       help='Number of trees in Random Forest (default: 100)')
    parser.add_argument('--max-depth', type=int, default=None,
                       help='Maximum depth of trees (default: None)')
    parser.add_argument('--random-state', type=int, default=42,
                       help='Random state for reproducibility (default: 42)')

    # Output arguments
    parser.add_argument('--model-dir', type=str, default='models',
                       help='Directory to save model (default: models)')
    parser.add_argument('--reports-dir', type=str, default='reports',
                       help='Directory to save metrics (default: reports)')
    parser.add_argument('--model-name', type=str, default=None,
                       help='Model name (default: auto-generated with timestamp)')

    # Training arguments
    parser.add_argument('--test-size', type=float, default=0.2,
                       help='Test split size (default: 0.2)')

    args = parser.parse_args()

    print(" Starting Mental Wellness Detection Model Training")
    print("=" * 60)

    # Generate model name if not provided
    if args.model_name is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.model_name = f"wellness_model_{timestamp}"

    # Load data
    print(" Loading data...")
    if args.data_path:
        # Load custom data
        if not os.path.exists(args.data_path):
            raise FileNotFoundError(f"Data file not found: {args.data_path}")
        df = pd.read_csv(args.data_path)
        print(f" Loaded custom data: {args.data_path}")
    else:
        # Use built-in data loader
        df = load_social_media_mental_health()
        print(" Loaded built-in social media mental health dataset")

    print(f"   Dataset shape: {df.shape}")

    # Preprocess data
    print("\n🔧 Preprocessing data...")
    encoded_df, wellness_df = preprocess_data(df)
    print(" Data preprocessing completed")

    # Prepare features and target
    target_col = "18. How often do you feel depressed or down?"
    X = encoded_df.drop(columns=[target_col])
    y = encoded_df[target_col]

    print(f"   Features shape: {X.shape}")
    print(f"   Target distribution: {y.value_counts().to_dict()}")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=args.random_state
    )
    print(f"   Train set: {X_train.shape[0]} samples")
    print(f"   Test set: {X_test.shape[0]} samples")

    # Model parameters
    model_params = {
        'n_estimators': args.n_estimators,
        'max_depth': args.max_depth,
        'random_state': args.random_state
    }

    print(f"\n Training model with parameters: {model_params}")

    # Train model
    model = train_model(X_train, y_train, model_params)
    print("✅ Model training completed")

    # Evaluate model
    print("\n📈 Evaluating model...")
    metrics = evaluate_model(model, X_test, y_test)

    print(f"   Accuracy: {metrics['accuracy']:.4f}")
    print(f"   Precision: {metrics['precision']:.4f}")
    print(f"   Recall: {metrics['recall']:.4f}")
    print(f"   F1 Score: {metrics['f1_score']:.4f}")
    # Save model and metrics
    model_path = os.path.join(args.model_dir, f"{args.model_name}.joblib")
    metrics_path = os.path.join(args.reports_dir, f"{args.model_name}_metrics.json")

    save_model_and_metrics(model, metrics, model_path, metrics_path)

    print("\nTraining completed successfully!")
    print(f"   Model: {model_path}")
    print(f"   Metrics: {metrics_path}")

    # Print final summary
    print("\n Training Summary:")
    print(f"   Model: {args.model_name}")
    print(f"   Accuracy: {metrics['accuracy']:.4f}")
    print(f"   F1 Score: {metrics['f1_score']:.4f}")
    print(f"   Training samples: {len(X_train)}")
    print(f"   Test samples: {len(X_test)}")


if __name__ == '__main__':
    main()