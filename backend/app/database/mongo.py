from pymongo import MongoClient
from app.config import MONGO_URI, db_name

client = MongoClient(MONGO_URI)
db = client[db_name]

usage_collection = db["demands"]
allocation_collection = db["allocations"]
network_state_collection = db["network_state"]
