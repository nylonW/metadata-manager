# test_metadata_manager.py

import unittest
import os
import json
import arrow 
from metadata_manager import MetadataManager

class TestMetadataManager(unittest.TestCase):

    def setUp(self):
        self.channelId = "test_channel"
        current_folder = os.path.dirname(os.path.abspath(__file__))
        self.store_file = current_folder +  "/test_store_file.json"
        self.manager = MetadataManager(self.channelId, self.store_file)

    def tearDown(self):
        if os.path.exists(self.store_file):
            os.remove(self.store_file)

    def test_get_next_publish_date_default(self):
        next_date = self.manager.get_next_publish_date()
        self.assertTrue(isinstance(next_date, str))

        with open(self.store_file, 'r') as f:
            data = json.load(f)
        self.assertIn(self.channelId, data)

    def test_get_next_publish_date_custom_hours(self):
        self.manager.get_next_publish_date()  # First call
        next_date_48h = self.manager.get_next_publish_date(1)
        expected_date = arrow.now().shift(hours=1)
        self.assertEqual(next_date_48h, expected_date.isoformat())

if __name__ == "__main__":
    unittest.main()
