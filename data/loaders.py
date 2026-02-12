"""
Robust data loading utilities for Mental Wellness Detection datasets.

This module provides functions to load and validate datasets from the Datasets/
directory with comprehensive error checking and data validation.
"""

import pandas as pd
import os
from typing import Tuple, Optional
from pathlib import Path


class DataLoaderError(Exception):
    """Custom exception for data loading errors."""
    pass


def _validate_dataframe(df: pd.DataFrame, expected_columns: list, dataset_name: str) -> None:
    """
    Validate dataframe structure and content.

    Args:
        df: DataFrame to validate
        expected_columns: List of expected column names
        dataset_name: Name of the dataset for error messages

    Raises:
        DataLoaderError: If validation fails
    """
    if df.empty:
        raise DataLoaderError(f"{dataset_name}: DataFrame is empty")

    if len(df) == 0:
        raise DataLoaderError(f"{dataset_name}: No rows found")

    # Check for expected columns (allow subset)
    missing_columns = [col for col in expected_columns if col not in df.columns]
    if missing_columns:
        raise DataLoaderError(f"{dataset_name}: Missing expected columns: {missing_columns}")

    # Check for excessive missing values
    missing_percent = df.isnull().sum().sum() / (len(df) * len(df.columns)) * 100
    if missing_percent > 50:
        raise DataLoaderError(f"{dataset_name}: Too many missing values ({missing_percent:.1f}%)")

    print(f"✅ {dataset_name}: Validation passed - {len(df)} rows, {len(df.columns)} columns")


def _get_data_path(*path_parts: str) -> Path:
    """
    Get absolute path to data file.

    Args:
        *path_parts: Path components relative to Datasets/

    Returns:
        Absolute path to the data file

    Raises:
        DataLoaderError: If file doesn't exist
    """
    base_path = Path(__file__).parent.parent / "Datasets"
    full_path = base_path / Path(*path_parts)

    if not full_path.exists():
        raise DataLoaderError(f"Data file not found: {full_path}")

    return full_path


def load_social_media_mental_health() -> pd.DataFrame:
    """
    Load the Social Media & Mental Health dataset.

    Returns:
        DataFrame containing the mental health survey data

    Raises:
        DataLoaderError: If loading or validation fails
    """
    try:
        file_path = _get_data_path("Social media & Mental Health", "smmh.csv")
        df = pd.read_csv(file_path)

        # Expected columns for validation
        expected_columns = [
            'Timestamp', '1. What is your age?', '2. Gender',
            '3. Relationship Status', '4. Occupation Status'
        ]

        _validate_dataframe(df, expected_columns, "Social Media & Mental Health")
        return df

    except Exception as e:
        if isinstance(e, DataLoaderError):
            raise
        raise DataLoaderError(f"Failed to load Social Media & Mental Health dataset: {str(e)}")


def load_train() -> pd.DataFrame:
    """
    Load the training dataset for Social Media Usage & Emotional Well-Being.

    Returns:
        DataFrame containing the training data

    Raises:
        DataLoaderError: If loading or validation fails
    """
    try:
        file_path = _get_data_path("Social Media Usage & Emotional Well-Being", "train.csv")
        df = pd.read_csv(file_path, on_bad_lines='skip')

        # Expected columns for validation
        expected_columns = ['User_ID', 'Age', 'Gender', 'Platform', 'Daily_Usage_Time (minutes)']

        _validate_dataframe(df, expected_columns, "Training Dataset")
        return df

    except Exception as e:
        if isinstance(e, DataLoaderError):
            raise
        raise DataLoaderError(f"Failed to load training dataset: {str(e)}")


def load_val() -> pd.DataFrame:
    """
    Load the validation dataset for Social Media Usage & Emotional Well-Being.

    Returns:
        DataFrame containing the validation data

    Raises:
        DataLoaderError: If loading or validation fails
    """
    try:
        file_path = _get_data_path("Social Media Usage & Emotional Well-Being", "val.csv")
        df = pd.read_csv(file_path, on_bad_lines='skip')

        # Expected columns for validation
        expected_columns = ['User_ID', 'Age', 'Gender', 'Platform', 'Daily_Usage_Time (minutes)']

        _validate_dataframe(df, expected_columns, "Validation Dataset")
        return df

    except Exception as e:
        if isinstance(e, DataLoaderError):
            raise
        raise DataLoaderError(f"Failed to load validation dataset: {str(e)}")


def load_test() -> pd.DataFrame:
    """
    Load the test dataset for Social Media Usage & Emotional Well-Being.

    Returns:
        DataFrame containing the test data

    Raises:
        DataLoaderError: If loading or validation fails
    """
    try:
        file_path = _get_data_path("Social Media Usage & Emotional Well-Being", "test.csv")
        df = pd.read_csv(file_path, on_bad_lines='skip')

        # Expected columns for validation
        expected_columns = ['User_ID', 'Age', 'Gender', 'Platform', 'Daily_Usage_Time (minutes)']

        _validate_dataframe(df, expected_columns, "Test Dataset")
        return df

    except Exception as e:
        if isinstance(e, DataLoaderError):
            raise
        raise DataLoaderError(f"Failed to load test dataset: {str(e)}")


def load_all_splits() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Load all train/validation/test splits at once.

    Returns:
        Tuple of (train_df, val_df, test_df)

    Raises:
        DataLoaderError: If any dataset fails to load
    """
    train_df = load_train()
    val_df = load_val()
    test_df = load_test()

    print(f"✅ All datasets loaded successfully:")
    print(f"   Train: {len(train_df)} samples")
    print(f"   Validation: {len(val_df)} samples")
    print(f"   Test: {len(test_df)} samples")

    return train_df, val_df, test_df


def get_dataset_info() -> dict:
    """
    Get information about available datasets.

    Returns:
        Dictionary with dataset information
    """
    info = {
        "social_media_mental_health": {
            "path": "Datasets/Social media & Mental Health/smmh.csv",
            "description": "Mental health survey responses related to social media usage"
        },
        "social_media_usage": {
            "path": "Datasets/Social Media Usage & Emotional Well-Being/",
            "description": "Social media usage patterns and emotional well-being data",
            "splits": {
                "train": "train.csv",
                "validation": "val.csv",
                "test": "test.csv"
            }
        }
    }
    return info