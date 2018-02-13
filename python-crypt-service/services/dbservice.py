from __future__ import print_function
from configurations import configuration
from pymongo import MongoClient

MONGO_HOST= configuration.MONGO_HOST
client = MongoClient(MONGO_HOST)

class DBConnection():

   def getConnection(self):
        return client.analyticsDB

