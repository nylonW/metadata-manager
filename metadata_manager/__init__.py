# metadata_manager.py

import os
import json
import hashlib
from datetime import datetime, timedelta

class MetadataManager:
    def __init__(self, channelId, store_file):
        self.channelId = channelId
        self.store_file = store_file
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.store_file):
            with open(self.store_file, 'r') as f:
                return json.load(f)
        return {}

    def save_data(self):
        with open(self.store_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_next_publish_date(self, hours=24):
        last_publish_date = self.data.get(self.channelId, None)
        if last_publish_date:
            last_publish_date = datetime.strptime(last_publish_date, "%Y-%m-%dT%H:%M:%S")
            next_publish_date = last_publish_date + timedelta(hours=hours)
        else:
            next_publish_date = datetime.utcnow()

        # Store the next publish date
        self.data[self.channelId] = next_publish_date.strftime("%Y-%m-%dT%H:%M:%S")
        self.save_data()

        return next_publish_date

def get_channel_id_from_secrets(secrets_path):
    with open(secrets_path, 'r') as f:
        content = f.read()
    return hashlib.md5(content.encode()).hexdigest()

# Usage example:
# channelId = get_channel_id_from_secrets('path_to/client_secrets.json')
# manager = MetadataManager(channelId, 'path_to/store_file.json')
# publish_at = manager.get_next_publish_date(48)  # For 48 hours