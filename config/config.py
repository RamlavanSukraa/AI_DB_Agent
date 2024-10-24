# config/config.py
import configparser
import os

# Initialize and read the config file
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))

# Fetch API Key, Database URL, and CSV Path
OPENAI_API_KEY = config.get('openai', 'api_key')
DATABASE_URL = config.get('database', 'url')
# CSV_PATH = config.get('files', 'csv_path')
