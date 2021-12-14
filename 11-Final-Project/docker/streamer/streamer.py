
"""
Streamer Module
This module returns tweets with metadata as json file and uploads to mongodb
"""

import json
import argparse
import tweepy
from credentials import CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import pymongo


parser = argparse.ArgumentParser()
parser.add_argument("keywords", type=str)
args = parser.parse_args()
kw = args.keywords


class Listener(tweepy.StreamListener):
    """Listener Object
    Uses the Stream class act on received data.
    Args:
        StreamListener (Class): Stream class sets connection.
    """
    def on_data(self, data): 
        self.process_data(data)
        return True


    def process_data(self, data):
        """Uploads tweets into MongoDB

        Args:
            data (BSON file): Twitter BSON files containint tweet info.
        """
        twt = json.loads(data) # data is inherent to tweepy class
        twt["search_kw"] = kw

        client = pymongo.MongoClient(host="mongodb", port=27017)
        db = client.twt # accesses database called twt_vac (on first call creates db)
        db.vac.insert_one(twt)


    def on_error(self, status_code):
        if status_code == 420:
            return False


class Stream():
    """Stream Object
    Sets connection between Twitter API and this code. Is used by
    the Listener Object to act on data received.
    """
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self, keyword_list):
        self.stream.filter(track=keyword_list, languages=["en"])




if __name__ == "__main__":

    AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    listener = Listener()
    stream = Stream(AUTH, listener)
    stream.start(keyword_list=kw)
