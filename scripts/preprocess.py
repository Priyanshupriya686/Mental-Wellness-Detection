#!/usr/bin/env python3
"""
Preprocessing utilities for Mental Wellness Detection.

This module contains data preprocessing functions used by training and inference scripts.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


# Wellness columns (same as in the notebook)
WELLNESS_COLS = [
    "11. Do you feel restless if you haven't used Social media in a while?",
    "12. On a scale of 1 to 5, how easily distracted are you?",
    "13. On a scale of 1 to 5, how much are you bothered by worries?",
    "14. Do you find it difficult to concentrate on things?",
    "15. On a scale of 1-5, how often do you compare yourself to other successful people through the use of social media?",
    "16. Following the previous question, how do you feel about these comparisons, generally speaking?",
    "17. How often do you look to seek validation from features of social media?",
    "18. How often do you feel depressed or down?",
    "19. On a scale of 1 to 5, how frequently does your interest in daily activities fluctuate?",
    "20. On a scale of 1 to 5, how often do you face issues regarding sleep?"
]

TARGET_COL = "18. How often do you feel depressed or down?"


def encode_wellness_data(df):
    """
    Encode categorical wellness columns using LabelEncoder.

    Args:
        df (pd.DataFrame): Input dataframe with wellness survey data

    Returns:
        pd.DataFrame: Encoded dataframe
    """
    # Filter to wellness columns that exist in the dataframe
    available_cols = [col for col in WELLNESS_COLS if col in df.columns]

    if not available_cols:
        raise ValueError("No wellness columns found in the input data")

    df_encoded = df[available_cols].apply(LabelEncoder().fit_transform)
    return df_encoded


def scale_wellness_data(df_encoded):
    """
    Scale the encoded wellness data using MinMaxScaler.

    Args:
        df_encoded (pd.DataFrame): Encoded dataframe

    Returns:
        pd.DataFrame: Scaled dataframe with wellness scores
    """
    scaler = MinMaxScaler()
    wellness_scaled = scaler.fit_transform(df_encoded.drop(columns=[TARGET_COL]) if TARGET_COL in df_encoded.columns else df_encoded)

    wellness_df = pd.DataFrame(wellness_scaled, columns=[f"Q{i+1}" for i in range(wellness_scaled.shape[1])])
    wellness_df['Wellness_Score'] = (1 - wellness_df.mean(axis=1)) * 100  # map 0-100

    def wellness_category(score):
        if score >= 75:
            return "High"
        elif score >= 50:
            return "Moderate"
        else:
            return "Low"

    wellness_df['Wellness_Level'] = wellness_df['Wellness_Score'].apply(wellness_category)

    return wellness_df


def preprocess_data(df):
    """
    Full preprocessing pipeline for training data.

    Args:
        df (pd.DataFrame): Raw input dataframe

    Returns:
        tuple: (encoded_df, wellness_df)
    """
    encoded_df = encode_wellness_data(df)
    wellness_df = scale_wellness_data(encoded_df)
    return encoded_df, wellness_df


def preprocess_for_inference(df):
    """
    Preprocessing pipeline for inference (prediction).

    Args:
        df (pd.DataFrame): Input dataframe for prediction

    Returns:
        pd.DataFrame: Preprocessed features ready for model prediction
    """
    encoded_df = encode_wellness_data(df)

    # For inference, we want to predict the target, so exclude it if present
    if TARGET_COL in encoded_df.columns:
        X = encoded_df.drop(columns=[TARGET_COL])
    else:
        X = encoded_df

    return X