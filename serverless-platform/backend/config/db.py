from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = None
db = None

def connect_to_mongo():
    global client, db
    client = MongoClient(MONGO_URI)
    db = client["serverless"]

def get_db():
    return db
