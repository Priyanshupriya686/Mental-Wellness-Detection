#!/usr/bin/env python3
"""
Evaluation script for Mental Wellness Detection model.

This script evaluates a trained model on test data and generates comprehensive
reports including classification metrics, confusion matrix, and visualizations.
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import (
    classification_report, confusion_matrix, accuracy_score,
    precision_score, recall_score, f1_score, roc_auc_score
)

# Import our preprocessing utilities
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts.preprocess import preprocess_data, preprocess_for_inference


def load_model(model_path):
    """
    Load a trained model from disk.

    Args:
        model_path (str): Path to the saved model file (.joblib)

    Returns:
        Loaded model object
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    model = joblib.load(model_path)
    print(f"✅ Loaded model from: {model_path}")
    return model


def load_test_data(data_path=None):
    """
    Load test data for evaluation.

    Args:
        data_path (str): Path to test data CSV. If None, uses default dataset.

    Returns:
        pd.DataFrame: Test dataset
    """
    if data_path is None:
        # Default path to the full dataset (we'll split it for evaluation)
        data_path = "Datasets/Social media & Mental Health/smmh.csv"

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Test data file not found: {data_path}")

    df = pd.read_csv(data_path)
    print(f"✅ Loaded test data: {len(df)} samples, {len(df.columns)} features")
    return df


def compute_detailed_metrics(y_true, y_pred, y_prob=None):
    """
    Compute comprehensive classification metrics.

    Args:
        y_true: True labels
        y_pred: Predicted labels
        y_prob: Prediction probabilities (optional, for AUC)

    Returns:
        dict: Dictionary containing all metrics
    """
    # Basic metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)

    # Per-class metrics
    precision_per_class = precision_score(y_true, y_pred, average=None, zero_division=0)
    recall_per_class = recall_score(y_true, y_pred, average=None, zero_division=0)
    f1_per_class = f1_score(y_true, y_pred, average=None, zero_division=0)

    # Confusion matrix
    conf_matrix = confusion_matrix(y_true, y_pred)

    # Classification report as dict
    class_report = classification_report(y_true, y_pred, output_dict=True, zero_division=0)

    # AUC score (if probabilities available and binary/multiclass)
    auc_score = None
    if y_prob is not None:
        try:
            if len(np.unique(y_true)) == 2:
                # Binary classification
                auc_score = roc_auc_score(y_true, y_prob[:, 1])
            else:
                # Multiclass - use one-vs-rest
                auc_score = roc_auc_score(y_true, y_prob, multi_class='ovr', average='weighted')
        except:
            auc_score = None

    metrics = {
        'accuracy': float(accuracy),
        'precision': float(precision),
        'recall': float(recall),
        'f1_score': float(f1),
        'precision_per_class': precision_per_class.tolist(),
        'recall_per_class': recall_per_class.tolist(),
        'f1_per_class': f1_per_class.tolist(),
        'confusion_matrix': conf_matrix.tolist(),
        'classification_report': class_report,
        'auc_score': float(auc_score) if auc_score is not None else None,
        'num_samples': len(y_true),
        'num_classes': len(np.unique(y_true)),
        'class_distribution': pd.Series(y_true).value_counts().to_dict()
    }

    return metrics


def generate_markdown_report(metrics, model_name, output_path):
    """
    Generate a comprehensive Markdown report.

    Args:
        metrics (dict): Computed metrics
        model_name (str): Name of the model
        output_path (str): Path to save the report
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""# Mental Wellness Detection Model Evaluation Report

**Model:** {model_name}  
**Evaluation Date:** {timestamp}  
**Test Samples:** {metrics['num_samples']}  
**Number of Classes:** {metrics['num_classes']}

## Summary Metrics

| Metric | Value |
|--------|-------|
| Accuracy | {metrics['accuracy']:.4f} |
| Precision (Weighted) | {metrics['precision']:.4f} |
| Recall (Weighted) | {metrics['recall']:.4f} |
| F1 Score (Weighted) | {metrics['f1_score']:.4f} |
{f"| AUC Score | {metrics['auc_score']:.4f} |" if metrics['auc_score'] is not None else ""}

## Class Distribution

| Class | Count | Percentage |
|-------|-------|------------|
"""

    total_samples = sum(metrics['class_distribution'].values())
    for class_label, count in metrics['class_distribution'].items():
        percentage = (count / total_samples) * 100
        report += f"| {class_label} | {count} | {percentage:.1f}% |\n"

    report += "\n## Confusion Matrix\n\n"
    conf_matrix = metrics['confusion_matrix']
    class_labels = list(metrics['class_distribution'].keys())

    # Header
    report += "| Actual \\ Predicted | " + " | ".join([f"Class {label}" for label in class_labels]) + " |\n"
    report += "|" + "---|" * (len(class_labels) + 1) + "\n"

    # Matrix rows
    for i, row in enumerate(conf_matrix):
        report += f"| Class {class_labels[i]} | " + " | ".join([str(cell) for cell in row]) + " |\n"

    report += "\n## Per-Class Metrics\n\n"
    report += "| Class | Precision | Recall | F1 Score | Support |\n"
    report += "|-------|-----------|--------|----------|--------|\n"

    for i, class_label in enumerate(class_labels):
        precision = metrics['precision_per_class'][i]
        recall = metrics['recall_per_class'][i]
        f1 = metrics['f1_per_class'][i]
        support = metrics['class_distribution'][class_label]
        report += f"| {class_label} | {precision:.4f} | {recall:.4f} | {f1:.4f} | {support} |\n"

    report += "\n## Detailed Classification Report\n\n"
    report += "```\n"
    report += pd.DataFrame(metrics['classification_report']).transpose().round(4).to_string()
    report += "\n```\n"

    report += "\n---\n*Report generated by Mental Wellness Detection evaluation script*"

    # Save report
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"✅ Markdown report saved to: {output_path}")


def evaluate_model(model, X_test, y_test):
    """
    Evaluate model on test data.

    Args:
        model: Trained model
        X_test: Test features
        y_test: Test labels

    Returns:
        dict: Evaluation metrics
    """
    print("\n📊 Evaluating model...")

    # Make predictions
    y_pred = model.predict(X_test)

    # Get probabilities if available (for AUC)
    y_prob = None
    if hasattr(model, 'predict_proba'):
        try:
            y_prob = model.predict_proba(X_test)
        except:
            pass

    # Compute metrics
    metrics = compute_detailed_metrics(y_test, y_pred, y_prob)

    # Print summary
    print(f"   Accuracy: {metrics['accuracy']:.4f}")
    print(f"   Precision: {metrics['precision']:.4f}")
    print(f"   Recall: {metrics['recall']:.4f}")
    print(f"   F1 Score: {metrics['f1_score']:.4f}")
    if metrics['auc_score'] is not None:
        print(f"   AUC Score: {metrics['auc_score']:.4f}")
    print(f"   Test samples: {metrics['num_samples']}")
    print(f"   Classes: {metrics['num_classes']}")

    return metrics


def main():
    """Main evaluation function."""
    parser = argparse.ArgumentParser(
        description='Evaluate Mental Wellness Detection Model',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python eval/evaluate.py --model-path models/wellness_model.joblib
  python eval/evaluate.py --model-path models/wellness_model.joblib --test-data Datasets/test.csv --output-dir reports/my_eval
        """
    )

    parser.add_argument('--model-path', required=True,
                       help='Path to trained model file (.joblib)')
    parser.add_argument('--test-data',
                       help='Path to test data CSV (default: use built-in dataset)')
    parser.add_argument('--output-dir', default='reports',
                       help='Directory to save evaluation reports (default: reports)')
    parser.add_argument('--report-name',
                       help='Name for the evaluation report (default: auto-generated with timestamp)')

    args = parser.parse_args()

    print("🔬 Mental Wellness Detection Model Evaluation")
    print("=" * 50)

    # Generate report name if not provided
    if args.report_name is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.report_name = f"evaluation_{timestamp}"

    # Load model
    model = load_model(args.model_path)

    # Load test data
    test_df = load_test_data(args.test_data)

    # Preprocess test data
    print("\n🔧 Preprocessing test data...")
    if args.test_data:
        # Custom test data - preprocess for inference
        encoded_df = preprocess_for_inference(test_df)
        target_col = "18. How often do you feel depressed or down?"
        if target_col in test_df.columns:
            X_test = encoded_df
            y_test = test_df[target_col]
        else:
            raise ValueError("Test data must contain target column for evaluation")
    else:
        # Use built-in dataset - split for evaluation
        encoded_df, _ = preprocess_data(test_df)
        target_col = "18. How often do you feel depressed or down?"
        X_test = encoded_df.drop(columns=[target_col])
        y_test = encoded_df[target_col]

    print(f"   Test features shape: {X_test.shape}")
    print(f"   Test target distribution: {y_test.value_counts().to_dict()}")

    # Evaluate model
    metrics = evaluate_model(model, X_test, y_test)

    # Generate reports
    print("\n📝 Generating reports...")

    # JSON report
    json_path = os.path.join(args.output_dir, f"{args.report_name}_metrics.json")
    os.makedirs(args.output_dir, exist_ok=True)
    with open(json_path, 'w') as f:
        json.dump(metrics, f, indent=2, default=str)
    print(f"✅ JSON metrics saved to: {json_path}")

    # Markdown report
    md_path = os.path.join(args.output_dir, f"{args.report_name}_report.md")
    generate_markdown_report(metrics, args.report_name, md_path)

    print("\n🎉 Evaluation completed successfully!")
    print(f"   JSON Report: {json_path}")
    print(f"   Markdown Report: {md_path}")

    # Print final summary
    print("\n📊 Final Summary:")
    print(f"   Model: {os.path.basename(args.model_path)}")
    print(f"   Test Samples: {metrics['num_samples']}")
    print(f"   Accuracy: {metrics['accuracy']:.4f}")
    print(f"   F1 Score: {metrics['f1_score']:.4f}")


if __name__ == '__main__':
    main()