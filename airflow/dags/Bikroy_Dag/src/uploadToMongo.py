import json
from pymongo import MongoClient

def upload_to_mongo():
    with open("mobiles_filtered.json", "r") as f:
        mobiles = json.load(f)

    with MongoClient('mongo', 27017) as client:
        db = client["BikroyDotCom"]
        collection = db["Mobiles"]
        if len(mobiles) > 0:
            collection.insert_many(mobiles)
            collection.create_index("url", unique=True)
