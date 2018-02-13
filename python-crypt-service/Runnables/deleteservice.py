
#db.user_track.remove( { access_time : {"$lt" : new Date(year, month_0_indexed, day)} })
#db.user_track.remove( { access_time : {"$lt" : new Date(2013, 8, 1) } })

from __future__ import print_function
from configurations import configuration
from services.dbservice import DBConnection
import schedule
import time

dbconnection = DBConnection();
print("Delete Service is Running...");
print("Delete Job will trigger in "+ str(configuration.TOTAL_MINS) +" min, After Data reached its Threshold of "+ str(configuration.TRIGGER_DELETE_AFTER_TOTAL_RECORDS_IN_DB) + "," + str(configuration.TOTAL_RECORDS_DELETE)+" records will be deleted");

def job():
  print("Cleaning in progress...");
  try:
    if dbconnection.getConnection().twittersearch.find().count() >= configuration.TRIGGER_DELETE_AFTER_TOTAL_RECORDS_IN_DB:
       for item in dbconnection.getConnection().twittersearch.find().limit(configuration.TOTAL_RECORDS_DELETE):
            dbconnection.getConnection().twittersearch.remove( { '_id' : item } )
            print("Cleaning done.");
  except Exception as e:
    print(e)

#schedule.every(configurations.TOTAL_SECS).seconds.do(job)
schedule.every(configuration.TOTAL_MINS).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


