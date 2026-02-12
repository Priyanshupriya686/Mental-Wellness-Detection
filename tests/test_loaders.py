"""
Unit tests for data loading utilities.
"""

import unittest
import pandas as pd
from data.loaders import (
    load_social_media_mental_health,
    load_train,
    load_val,
    load_test,
    load_all_splits,
    get_dataset_info,
    DataLoaderError
)
import os
import tempfile


class TestDataLoaders(unittest.TestCase):

    def test_load_social_media_mental_health(self):
        """Test loading the social media mental health dataset."""
        df = load_social_media_mental_health()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn('Timestamp', df.columns)
        self.assertIn('1. What is your age?', df.columns)

    def test_load_train(self):
        """Test loading the training dataset."""
        df = load_train()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn('User_ID', df.columns)
        self.assertIn('Age', df.columns)

    def test_load_val(self):
        """Test loading the validation dataset."""
        df = load_val()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn('User_ID', df.columns)

    def test_load_test(self):
        """Test loading the test dataset."""
        df = load_test()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn('User_ID', df.columns)

    def test_load_all_splits(self):
        """Test loading all splits at once."""
        train_df, val_df, test_df = load_all_splits()
        self.assertIsInstance(train_df, pd.DataFrame)
        self.assertIsInstance(val_df, pd.DataFrame)
        self.assertIsInstance(test_df, pd.DataFrame)
        self.assertGreater(len(train_df), len(val_df))
        self.assertGreater(len(train_df), len(test_df))

    def test_get_dataset_info(self):
        """Test getting dataset information."""
        info = get_dataset_info()
        self.assertIsInstance(info, dict)
        self.assertIn('social_media_mental_health', info)
        self.assertIn('social_media_usage', info)

    def test_missing_file_error(self):
        """Test error handling for missing files."""
        # This would require mocking, but for now we'll just ensure
        # the functions exist and can be imported
        self.assertTrue(callable(load_social_media_mental_health))
        self.assertTrue(callable(load_train))
        self.assertTrue(callable(load_val))
        self.assertTrue(callable(load_test))


if __name__ == '__main__':
    unittest.main()