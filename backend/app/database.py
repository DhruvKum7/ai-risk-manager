import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = MongoClient(MONGODB_URL)

db = client[DATABASE_NAME]

chargebacks_collection = db["chargebacks"]
transactions_collection = db["transactions"]
orders_collection = db["orders"]
customers_collection = db["customers"]
evidence_collection = db["evidence"]
risk_results_collection = db["risk_results"]