import redis_connection
import json
import mongo_connection
from datetime import datetime

r = redis_connection.connect_to_redis()

coll = mongo_connection.get_collection()

while True:
    if len(r.lrange("urgent_queue", 0, -1)) != 0:
        alert_redis = r.brpop(['urgent_queue'])
        alert_dict = json.loads(alert_redis[1])
        print(f"pulled alert from redis urgent")
        alert_dict["insertion_time"] = datetime.now()
        print("added insertion time")
        coll.insert_one(alert_dict)
        print(f"inserted into mongo")
        print("\n-------------------------------------\n")
        continue
    else:
        alert_redis = r.brpop(['normal_queue'])
        alert_dict = json.loads(alert_redis[1])
        print(f"pulled alert from redis normal")
        alert_dict["insertion_time"] = datetime.now()
        print("added insertion time")
        coll.insert_one(alert_dict)
        print(f"inserted into mongo")
        print("\n-------------------------------------\n")
        continue

