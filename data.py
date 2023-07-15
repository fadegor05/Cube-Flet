import asyncio
import json
from config import *

# Save function
def save_json(file, data):
    with open(file, "w") as my_file:
        my_file.write(json.dumps(data))

# Load function
def load_json(file):
    with open(file, "r") as my_file:
        return json.loads(my_file.read())