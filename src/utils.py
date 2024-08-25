import os.path
import json
from config import DATA_PATH

def get_data_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception:
        return []

print(get_data_json(os.path.join(DATA_PATH, 'operations.json')))