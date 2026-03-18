import os
import sys
import json

from dotenv import load_dotenv

import certifi
import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


ca=certifi.where()  ## Certificate authority bundle path

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

# ETL pipeline
class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    # CSV to JSON convertor function
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    # Function to insert data into MongoDB
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        


if __name__ == "__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="ANKITAI"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(FILE_PATH)
    print(f"{len(records)} records extracted from the csv file successfully")
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(f"{no_of_records} records inserted successfully in MongoDB database {DATABASE} and collection {Collection}")