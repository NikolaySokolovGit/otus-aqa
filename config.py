import json
from pathlib import Path

with open(str(Path(__file__).resolve().parent)+"/config.json") as file:
    config = json.load(file)
