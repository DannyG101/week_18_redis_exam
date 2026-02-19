import mongo_connection
import redis_connection
import json

r = redis_connection.connect_to_redis()
collection = mongo_connection.get_collection()



def get_alerts_by_border_and_priority():
    redis_key = "alerts_by_border_and_priority"
    redis_alert = r.get(redis_key)
    if redis_alert:
        redis_alert_json = json.dumps(redis_alert)
        return redis_alert_json
    else:
        mongo_data = collection.get({}, {"_id":0})
        r.setex(redis_key, 3600, json.dumps(mongo_data))
        return list(mongo_data)

def get_top_urgent_zones():
    redis_key = "top_urgent_zones"
    redis_alert = r.get(redis_key)
    if redis_alert:
        redis_alert_json = json.dumps(redis_alert)
        return redis_alert_json
    else:
        mongo_data = collection.get({}, {"_id": 0})
        r.setex(redis_key, 3600, json.dumps(mongo_data))
        return list(mongo_data)

def get_distance_distribution():
    redis_key = "distance_distribution"
    redis_alert = r.get(redis_key)
    if redis_alert:
        redis_alert_json = json.dumps(redis_alert)
        return redis_alert_json
    else:
        mongo_data = collection.get({}, {"_id": 0})
        r.setex(redis_key, 3600, json.dumps(mongo_data))
        return list(mongo_data)

def get_low_visibility_high_activity():
    redis_key = "low_visibility_high_activity"
    redis_alert = r.get(redis_key)
    if redis_alert:
        redis_alert_json = json.dumps(redis_alert)
        return redis_alert_json
    else:
        mongo_data = collection.get({}, {"_id": 0})
        r.setex(redis_key, 3600, json.dumps(mongo_data))
        return list(mongo_data)

def get_hot_zones():
    redis_key = "hot_zones"
    redis_alert = r.get(redis_key)
    if redis_alert:
        redis_alert_json = json.dumps(redis_alert)
        return redis_alert_json
    else:
        mongo_data = collection.get({}, {"_id": 0})
        r.setex(redis_key, 3600, json.dumps(mongo_data))
        return list(mongo_data)



