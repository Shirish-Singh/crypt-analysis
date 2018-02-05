
#db.user_track.remove( { access_time : {"$lt" : new Date(year, month_0_indexed, day)} })
#db.user_track.remove( { access_time : {"$lt" : new Date(2013, 8, 1) } })

from __future__ import print_function
import tweepy
import json
import configurations
import keywords
from streamdata import StreamData
import tweet_utils
from pymongo import MongoClient
from datetime import datetime
import pytz
import schedule
import time
MONGO_HOST= configurations.MONGO_HOST

client = MongoClient(MONGO_HOST)
# Use twitterdb database. If it doesn't exist, it will be created.
db = client.twitterdb
print("Delete Service is Running...");
print("Delete Job will trigger in "+ str(configurations.TOTAL_MINS) +" min, After Data reached its Threshold of "+ str(configurations.TRIGGER_DELETE_AFTER_TOTAL_RECORDS_IN_DB) + "," + str(configurations.TOTAL_RECORDS_DELETE)+" records will be deleted");

def job():
  print("Cleaning in progress...");
  try:
    if db.twittersearch.find().count() >= configurations.TRIGGER_DELETE_AFTER_TOTAL_RECORDS_IN_DB:
       for item in db.twittersearch.find().limit(configurations.TOTAL_RECORDS_DELETE):
            db.twittersearch.remove( { '_id' : item } )
            print("Cleaning done.");
  except Exception as e:
    print(e)


#schedule.every(configurations.TOTAL_SECS).seconds.do(job)
schedule.every(configurations.TOTAL_MINS).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


