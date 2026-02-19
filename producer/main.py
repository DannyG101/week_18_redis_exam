from pydantic import BaseModel
from datetime import datetime
import json
import redis_connection
import priority_logic
from typing import Optional
from time import sleep


class Alert(BaseModel):
    border : str
    zone : str
    timestamp : datetime
    people_count : int
    weapons_count : int
    vehicle_type : str
    distance_from_fence_m : int
    visibility_quality : float
    priority : Optional[str] = None

r = redis_connection.connect_to_redis()

data = priority_logic.load_data()

for item in data:
    alert = Alert(**item)
    if alert.weapons_count > 0:
        alert.priority = "URGENT"
    elif alert.distance_from_fence_m <= 50:
        alert.priority = "URGENT"
    elif alert.people_count >= 8:
        alert.priority = "URGENT"
    elif alert.vehicle_type == "truck":
        alert.priority = "URGENT"
    elif alert.distance_from_fence_m <= 150 and alert.people_count >=4:
        alert.priority = "URGENT"
    elif alert.vehicle_type == "jeep" and alert.people_count >=3:
        alert.priority = "URGENT"
    else:
        alert.priority = "NORMAL"

    if alert.priority == "URGENT":
        r.lpush("urgent_queue", alert.model_dump_json())
        print("sent to urgent")
    else:
        r.lpush("normal_queue", alert.model_dump_json())
        print("sent to normal")





