# test_metadata_manager.py

import unittest
import os
import json
from datetime import datetime, timedelta
from metadata_manager import MetadataManager, get_channel_id_from_secrets

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
        self.assertTrue(isinstance(next_date, datetime))

        with open(self.store_file, 'r') as f:
            data = json.load(f)
        self.assertIn(self.channelId, data)

    def test_get_next_publish_date_custom_hours(self):
        self.manager.get_next_publish_date()  # First call
        next_date_48h = self.manager.get_next_publish_date(1)
        expected_date = datetime.utcnow() + timedelta(hours=1)
        self.assertAlmostEqual(next_date_48h.timestamp(), expected_date.timestamp(), delta=5)

    def test_get_channel_id_from_secrets(self):
        test_secrets_content = '{"test_key": "test_value"}'
        test_secrets_path = "test_secrets.json"
        with open(test_secrets_path, 'w') as f:
            f.write(test_secrets_content)

        channel_id = get_channel_id_from_secrets(test_secrets_path)
        self.assertEqual(len(channel_id), 32)  # MD5 hash length

        os.remove(test_secrets_path)

if __name__ == "__main__":
    unittest.main()
