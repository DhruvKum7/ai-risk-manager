import json

from app.database import (
    transactions_collection,
    orders_collection,
    customers_collection
)


with open("../data/sample_data.json", "r") as file:
    data = json.load(file)


transactions_collection.delete_many({})
orders_collection.delete_many({})
customers_collection.delete_many({})


if data["transactions"]:
    transactions_collection.insert_many(data["transactions"])

if data["orders"]:
    orders_collection.insert_many(data["orders"])

if data["customers"]:
    customers_collection.insert_many(data["customers"])


print("Sample data inserted successfully!")