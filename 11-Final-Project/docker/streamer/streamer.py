
import tweepy
from credentials import CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import json
import logging
import pymongo


keyword_list = ["Pfizer","AstraZeneca","J&J","Moderna"]


class Listener(tweepy.StreamListener):
    def on_data(self, data): 
        self.process_data(data)
        return True

    def process_data(self, data):

        twt = json.loads(data) # data is inherent to tweepy class

        client = pymongo.MongoClient(host="mongodb", port=27017)
        db = client.twt # accesses database called twt_vac (on first call creates db)
        r = db.vac.insert_one(twt)
        # logging.critical(r)

    def on_error(self, status_code):
        if status_code == 420:
            return False


class Stream():
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self, keyword_list):
        self.stream.filter(track=keyword_list, languages=["en"])


if __name__ == "__main__":

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    listener = Listener()
    stream = Stream(auth, listener)
    
    stream.start(keyword_list=keyword_list)
