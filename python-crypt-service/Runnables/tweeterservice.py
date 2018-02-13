from __future__ import print_function
from  services.dbservice import DBConnection
import tweepy
import json
from configurations import configuration
from configurations import keywords
from models.streamdata import StreamData
from utils import tweetutils
from datetime import datetime
import pytz

CONSUMER_KEY = configuration.CONSUMER_KEY
CONSUMER_SECRET = configuration.CONSUMER_SECRET
ACCESS_TOKEN = configuration.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = configuration.ACCESS_TOKEN_SECRET
WORDS= keywords.WORDS
SRC_TYPE="TWEETER"
SPAM_KEYWORDS= keywords.SPAM
dbconnection = DBConnection();

def cleanData(datajson):
  text= tweetutils.get_some_text_cleaned(datajson);
  datajson['text']=text;
  return datajson;


def preProcessData(datajson):
  datajson = cleanData(datajson);
  return datajson;


def checkForSpam(datajson):
  for w in SPAM_KEYWORDS:
     if w  in datajson['text']:
      return "true";


class StreamListener(tweepy.StreamListener):
    # This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False


    def on_data(self, data):
        # This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            datajson=preProcessData(datajson);
            # grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']
            print("Tweet collected at " + str(created_at))

            hashtags = tweetutils.get_hashtags(datajson);
            #Create Stream Data Object and set values
            streamdata = StreamData();
            streamdata.keyword=hashtags;
            streamdata.data=datajson;
            streamdata.srcType=SRC_TYPE;
            streamdata.createdDate = datetime.now(pytz.timezone('Asia/Kolkata'));
            streamdata.status = "NEW"
            print(datetime.now(pytz.timezone('Asia/Kolkata')));
            # insert the data into the mongoDB into a collection
            # if collection doesn't exist, it will be created.
            #Notice the _dict_ below it takes object and converts into may be json which is stored in mongodb.
            if (checkForSpam(datajson)=='true'):
                    #db.spam.insert(streamdata.__dict__)
                    print("SPAM DETECTED!!!!!!!!!!!!!!!!!!!!!!")
            else:
              dbconnection.getConnection().twittersearch.insert(streamdata.__dict__)

        except Exception as e:
                print(e)


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
