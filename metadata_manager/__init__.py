# metadata_manager.py

import os
import json
import hashlib
import arrow

# Example metadata file
# {
#   "title": "my test title",
#   "description": "my test description",
#   "tags": ["test tag1", "test tag2"],
#   "privacyStatus": "private",
#   "madeForKids": false,
#   "publicStatsViewable": true,
#   "publishAt": "2017-06-01T12:05:00+02:00",
#   "categoryId": "22", // people and blogs
#   "language":  "en"
# }

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

    # desired format everythere '2020-11-25T08:10:39.672624+01:00'
    def get_next_publish_date(self, hours=24):
        last_publish_date = self.data.get(self.channelId, None)
        if last_publish_date:
            last_publish_date = arrow.get(last_publish_date)
            next_publish_date = last_publish_date.shift(hours=hours)
        else:
            next_publish_date = arrow.now().isoformat()

        # Store the next publish date
        self.data[self.channelId] = arrow.get(next_publish_date).isoformat()
        self.save_data()

        return arrow.get(next_publish_date).isoformat()
    
    def get_metadata(self, title, description, tags):
        next_publish_date = self.get_next_publish_date()
        return {
            "title": title,
            "description": description,
            "tags": tags,
            "privacyStatus": "private",
            "madeForKids": "false",
            "publicStatsViewable": "true",
            "publishAt": next_publish_date,
            "categoryId": '22',
            "language":  'en'
        }
    
    def save_metadata_to_file(self, path, file_name, metadata):
        # remember to create folders if folders not exists
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = os.path.join(path, file_name)
        with open(file_path, 'w') as f:
            json.dump(metadata, f, indent=4)