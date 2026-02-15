#!/usr/bin/env python3
"""
Inference script for Mental Wellness Detection model.

This script loads a trained model and makes predictions on new data,
either from a single input or a CSV file.
"""

import argparse
import json
import os
from pathlib import Path

import pandas as pd
import joblib
import numpy as np

# Import our preprocessing utilities
from preprocess import preprocess_data


def load_model(model_path):
    """
    Load a trained model from disk.

    Args:
        model_path: Path to the saved model file

    Returns:
        Loaded model
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    model = joblib.load(model_path)
    print(f"✅ Model loaded from: {model_path}")
    return model


def preprocess_input_data(input_data, data_type='single'):
    """
    Preprocess input data for prediction.

    Args:
        input_data: Either a dict (single sample) or DataFrame (batch)
        data_type: 'single' or 'batch'

    Returns:
        Preprocessed features ready for prediction
    """
    if data_type == 'single':
        # Convert single input to DataFrame
        df = pd.DataFrame([input_data])
    else:
        # input_data is already a DataFrame
        df = input_data

    # Apply the same preprocessing as training
    encoded_df, _ = preprocess_data(df)

    # Prepare features (same as training)
    target_col = "18. How often do you feel depressed or down?"
    if target_col in encoded_df.columns:
        X = encoded_df.drop(columns=[target_col])
    else:
        X = encoded_df

    return X


def predict_single(model, input_data):
    """
    Make prediction on a single input sample.

    Args:
        model: Trained model
        input_data: Dictionary with feature values

    Returns:
        Prediction result
    """
    # Preprocess input
    X = preprocess_input_data(input_data, data_type='single')

    # Make prediction
    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]

    # Create result
    result = {
        'prediction': int(prediction),
        'probabilities': {f'class_{i}': float(prob) for i, prob in enumerate(probabilities)},
        'confidence': float(max(probabilities))
    }

    return result


def predict_batch(model, input_csv, output_csv):
    """
    Make predictions on a batch of data from CSV.

    Args:
        model: Trained model
        input_csv: Path to input CSV file
        output_csv: Path to output CSV file
    """
    # Load input data
    if not os.path.exists(input_csv):
        raise FileNotFoundError(f"Input CSV file not found: {input_csv}")

    df = pd.read_csv(input_csv)
    print(f"✅ Loaded input data: {len(df)} samples")

    # Preprocess data
    X = preprocess_input_data(df, data_type='batch')

    # Make predictions
    predictions = model.predict(X)
    probabilities = model.predict_proba(X)

    # Add predictions to dataframe
    df['predicted_depression_level'] = predictions

    # Add probability columns
    for i in range(probabilities.shape[1]):
        df[f'probability_class_{i}'] = probabilities[:, i]

    # Add confidence (max probability)
    df['prediction_confidence'] = np.max(probabilities, axis=1)

    # Save results
    output_dir = os.path.dirname(output_csv) or '.'
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f"✅ Predictions saved to: {output_csv}")

    # Print summary
    print("\n📊 Prediction Summary:")
    print(f"   Total samples: {len(df)}")
    print(f"   Predictions distribution: {pd.Series(predictions).value_counts().to_dict()}")

    return df


def create_sample_input():
    """
    Create a sample input for demonstration.

    Returns:
        Dictionary with sample feature values
    """
    sample = {
        "11. Do you feel restless if you haven't used Social media in a while?": 3,
        "12. On a scale of 1 to 5, how easily distracted are you?": 4,
        "13. On a scale of 1 to 5, how much are you bothered by worries?": 3,
        "14. Do you find it difficult to concentrate on things?": 2,
        "15. On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?": 3,
        "16. Following the previous question, how do you feel about these comparisons, generally speaking?": 2,
        "17. How often do you look to seek validation from features of social media?": 4,
        "18. How often do you feel depressed or down?": 2,  # This will be predicted
        "19. On a scale of 1 to 5, how frequently does your interest in daily activities fluctuate?": 3,
        "20. On a scale of 1 to 5, how often do you face issues regarding sleep?": 2
    }
    return sample


def main():
    parser = argparse.ArgumentParser(description='Mental Wellness Detection Inference')

    # Model arguments
    parser.add_argument('--model-path', type=str, required=True,
                       help='Path to trained model file (.joblib)')

    # Input arguments (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--input-csv', type=str,
                            help='Path to input CSV file for batch prediction')
    input_group.add_argument('--sample', action='store_true',
                            help='Use sample input for demonstration')

    # Output arguments
    parser.add_argument('--output-csv', type=str,
                       help='Path to output CSV file (for batch prediction)')

    args = parser.parse_args()

    print("🔮 Mental Wellness Detection Inference")
    print("=" * 50)

    # Load model
    try:
        model = load_model(args.model_path)
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return

    # Handle different input types
    if args.sample:
        # Single sample prediction
        print("\n📝 Using sample input for prediction...")
        sample_input = create_sample_input()

        print("Sample input features:")
        for key, value in sample_input.items():
            print(f"   {key}: {value}")

        try:
            result = predict_single(model, sample_input)

            print("\n🎯 Prediction Results:")
            print(f"   Predicted Depression Level: {result['prediction']}")
            print(f"   Confidence: {result['confidence']:.4f}")
            print("   Class Probabilities:")
            for class_name, prob in result['probabilities'].items():
                print(f"     {class_name}: {prob:.4f}")
        except Exception as e:
            print(f"❌ Error making prediction: {e}")

    elif args.input_csv:
        # Batch prediction
        if not args.output_csv:
            print("❌ Error: --output-csv is required for batch prediction")
            return

        print(f"\n📊 Processing batch prediction from: {args.input_csv}")

        try:
            results_df = predict_batch(model, args.input_csv, args.output_csv)
            print("✅ Batch prediction completed successfully!")

        except Exception as e:
            print(f"❌ Error processing batch prediction: {e}")

    else:
        parser.error("Must specify either --sample or --input-csv")


if __name__ == '__main__':
    main()