import json
from pymongo import MongoClient

def check_mongo_for_duplicates():
    with open("mobile_data.json", "r") as f:
        mobiles = json.load(f)

    new_urls = [mobile["url"] for mobile in mobiles]
    
    with MongoClient('mongo', 27017) as client:
        db = client["BikroyDotCom"]
        collection = db["Mobiles"]
        existing_urls = collection.find({}, {"url":True})
        existing_urls = [url["url"] for url in existing_urls]
        duplicates = set(new_urls).intersection(existing_urls)

    filtered_mobiles = [mobile for mobile in mobiles if mobile["url"] not in duplicates]

    with open("mobiles_filtered.json", "w") as f:
        json.dump(filtered_mobiles, f)
        
        