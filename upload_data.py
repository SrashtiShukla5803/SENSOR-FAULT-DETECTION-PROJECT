from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#uri
uri="mongodb+srv://srashtishukla94:MPHiuOhTmHFBsQLe@cluster0.jb5zd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="sensor"

COLLECTION_NAME="waferfault"

df=pd.read_csv("C:\Users\HP\Downloads\SensorProject\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

type(json_record)

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)