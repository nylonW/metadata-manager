# Metadata Manager

`metadata_manager` is a Python library designed to manage the `metadata.json` across videos on YouTube channels. It helps in determining the next publish date for videos, ensuring a 24-hour gap between consecutive video uploads for a specific channel.

## Features

- Generates a unique `channelId` based on the hash of `client_secrets.json`.
- Manages and stores the last publish date for each channel.
- Calculates the next publish date, ensuring a 24-hour gap from the last publish date.

## Installation

Copy the `metadata_manager.py` to your project directory.

## Usage

### 1. Import the library

```python
import metadata_manager
```

### 2. Calculate the `channelId`

To generate a unique `channelId` based on the hash of `client_secrets.json`:

```python
channelId = metadata_manager.get_channel_id_from_secrets('path_to/client_secrets.json')
```

Replace `'path_to/client_secrets.json'` with the actual path to your `client_secrets.json` file.

### 3. Create an instance of `MetadataManager`

```python
manager = metadata_manager.MetadataManager(channelId, 'path_to/store_file.json')
```

Replace `'path_to/store_file.json'` with the path where you want to store the metadata information.

### 4. Get the next publish date

To get the next publish date for a video:

```python
publish_at = manager.get_next_publish_date()
print(publish_at)
```

This will return a `datetime` object representing the next publish date, ensuring a 24-hour gap from the last publish date for the specific channel.

## Example

```python
import metadata_manager

# Calculate channelId based on the hash of client_secrets.json
channelId = metadata_manager.get_channel_id_from_secrets('path_to/client_secrets.json')

# Create an instance of MetadataManager
manager = metadata_manager.MetadataManager(channelId, 'path_to/store_file.json')

# Get the next publish date
publish_at = manager.get_next_publish_date(48)
print(f"Next publish date: {publish_at}")
```

## License

This project is licensed under the MIT License.