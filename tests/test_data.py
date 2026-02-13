import unittest
from wmdetection.data.loader import load_data
from wmdetection.preprocess.preprocess import preprocess_data

class TestData(unittest.TestCase):
    def test_load_data(self):
        df = load_data()
        self.assertIsNotNone(df)
        self.assertGreater(len(df), 0)

    def test_preprocess_data(self):
        df = load_data()
        encoded_df, wellness_df = preprocess_data(df)
        self.assertIsNotNone(encoded_df)
        self.assertIsNotNone(wellness_df)
        self.assertIn('Wellness_Score', wellness_df.columns)

if __name__ == '__main__':
    unittest.main()