#!/usr/bin/env python3
"""
Example script demonstrating data loader usage.

This script shows how to use the robust data loading utilities
to load and inspect the Mental Wellness Detection datasets.
"""

from data import (
    load_social_media_mental_health,
    load_train,
    load_val,
    load_test,
    load_all_splits,
    get_dataset_info
)


def main():
    print("🔍 Mental Wellness Detection - Data Loader Example")
    print("=" * 50)

    # Show available datasets
    print("\n📊 Available Datasets:")
    info = get_dataset_info()
    for name, details in info.items():
        print(f"  • {name}: {details['description']}")
        if 'splits' in details:
            print("    Splits:", list(details['splits'].keys()))

    # Load social media mental health dataset
    print("\n📈 Loading Social Media & Mental Health Dataset...")
    try:
        smmh_df = load_social_media_mental_health()
        print(f"   Shape: {smmh_df.shape}")
        print(f"   Columns: {list(smmh_df.columns[:5])}...")
        print(f"   Sample age range: {smmh_df['1. What is your age?'].min():.0f} - {smmh_df['1. What is your age?'].max():.0f}")
    except Exception as e:
        print(f"   ❌ Error: {e}")

    # Load train/val/test splits
    print("\n🎯 Loading Social Media Usage & Emotional Well-Being Splits...")
    try:
        train_df, val_df, test_df = load_all_splits()

        print(f"   Train set: {train_df.shape[0]} samples")
        print(f"   Validation set: {val_df.shape[0]} samples")
        print(f"   Test set: {test_df.shape[0]} samples")

        # Show sample data
        print("\n📋 Sample from training data:")
        print(train_df[['User_ID', 'Age', 'Gender', 'Platform', 'Daily_Usage_Time (minutes)']].head(3))

    except Exception as e:
        print(f"   ❌ Error: {e}")

    print("\n✅ Data loading example completed!")


if __name__ == '__main__':
    main()