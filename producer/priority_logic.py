import json

def load_data():
    with open("../data/border_alerts.json") as f:
        return json.load(f)