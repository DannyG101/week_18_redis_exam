import json


def load_data():
    with open("border_alerts.json") as f:
        return json.load(f)


def priority_check(alert):
    if alert.weapons_count > 0:
        alert.priority = "URGENT"
    elif alert.distance_from_fence_m <= 50:
        alert.priority = "URGENT"
    elif alert.people_count >= 8:
        alert.priority = "URGENT"
    elif alert.vehicle_type == "truck":
        alert.priority = "URGENT"
    elif alert.distance_from_fence_m <= 150 and alert.people_count >= 4:
        alert.priority = "URGENT"
    elif alert.vehicle_type == "jeep" and alert.people_count >= 3:
        alert.priority = "URGENT"
    else:
        alert.priority = "NORMAL"
    return alert