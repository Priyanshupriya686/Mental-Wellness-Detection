import pandas as pd
import os

def load_data(data_path=None):
    """
    Load the social media mental health dataset.

    Args:
        data_path (str): Path to the CSV file. If None, uses default path.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    if data_path is None:
        # Default path relative to package
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_path = os.path.join(base_dir, 'Datasets', 'Social media & Mental Health', 'smmh.csv')

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found at {data_path}")

    df = pd.read_csv(data_path)
    print("Loaded dataset")
    print("Shape:", df.shape)
    return df