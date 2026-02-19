import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_USER = os.getenv("MONGO_USER", "root")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "example")
MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"
print(MONGO_URI)

def get_collection():
    client = MongoClient(MONGO_URI)
    db = client["alerts_db"]
    collection = db["alerts_coll"]
    return collection

