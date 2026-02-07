from pymongo.mongo_client import MongoClient
from app.config import MONGO_URI, db_name

client = MongoClient(MONGO_URI)
db = client(db_name)

demands_set = db["demands"]
allocations_set = db["allocations"]
network_state_set = db["network_state"]