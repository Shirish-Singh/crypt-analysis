from __future__ import print_function

import pymongo
from textblob import TextBlob
from configurations import configuration
from services.dbservice import DBConnection
import schedule
import time
from models.sentimentdata import SentimentData

dbconnection = DBConnection();
print("Sentiment Service is Running...");


def insertIntoDB(polarity, record,text):
  sentimentdata = SentimentData();
  sentimentdata.lang =  record.get("data").get("lang")
  sentimentdata.keywords = record.get("keyword")
  sentimentdata.text = text
  if (polarity == 0):
     sentimentdata.neutral=1;
  if (polarity > 0):
    sentimentdata.positive = polarity;
  if (polarity < 0):
    sentimentdata.negative = polarity;
  dbconnection.getConnection().sentiments.insert(sentimentdata.__dict__)

def job():
  print("Sentiment analysis from DB in progress...");
  try:
      records = dbconnection.getConnection().twittersearch.find(modifiers={"$snapshot" : True}).limit(10)
      for record in records:
          if (record.get("data").get("extended_tweet") != None):
            text = record.get("data").get("extended_tweet").get("full_text")
          else:
             text = record.get("data").get("text")
          blob = TextBlob(record.get("data").get("text"))
          for sentence in blob.sentences:
           print(sentence.sentiment.polarity)
           insertIntoDB(sentence.sentiment.polarity,record,text)
  except Exception as e:
      print(e)

#schedule.every(configurations.TOTAL_SECS).seconds.do(job)
schedule.every(configuration.TOTAL_SECS_FOR_SENTIMENT).seconds.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

