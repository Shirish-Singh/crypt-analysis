from __future__ import print_function
import tweepy
import json
import configurations
import keywords
from streamdata import StreamData
import tweet_utils
from pymongo import MongoClient

MONGO_HOST= configurations.MONGO_HOST
CONSUMER_KEY = configurations.CONSUMER_KEY
CONSUMER_SECRET = configurations.CONSUMER_SECRET
ACCESS_TOKEN = configurations.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = configurations.ACCESS_TOKEN_SECRET
WORDS=keywords.WORDS
SRC_TYPE="TWEETER"


def cleanData(datajson):
  text=tweet_utils.get_some_text_cleaned(datajson);
  print("-------------Tweet Cleaned Before " + datajson['text'] + " After " +text );
  datajson['text']=text;
  return datajson;


def preProcessData(datajson):
  datajson = cleanData(datajson);
  return datajson;



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
            streamdata = StreamData();
            client = MongoClient(MONGO_HOST)
            # Use twitterdb database. If it doesn't exist, it will be created.
            db = client.twitterdb

            # Decode the JSON from Twitter
            datajson = json.loads(data)
            datajson=preProcessData(datajson);
            # grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']
            print("Tweet collected at " + str(created_at))

            hashtags = tweet_utils.get_hashtags(datajson);
            #Create Stream Data Object and set values
            streamdata.keyword=hashtags;
            streamdata.data=datajson;
            streamdata.srcType=SRC_TYPE;

            # insert the data into the mongoDB into a collection
            # if collection doesn't exist, it will be created.
            #Notice the _dict_ below it takes object and converts into may be json which is stored in mongodb.
            db.twittersearch.insert((streamdata.__dict__))
        except Exception as e:
            print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
