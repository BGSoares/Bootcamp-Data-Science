import tweepy
import credentials
import pymongo
import json
import logging


class Listener(tweepy.StreamListener):
    def on_data(self, data): 
        self.process_data(data)
        return True

    def process_data(self, data):
        
        client = pymongo.MongoClient(host="mongodb", port=27017) # connects to mongodb container
        db = client.twitter # connects to twitter database (on first time creates db)

        tweet = json.loads(data) # inserts tweet into tweets collection (on first time creates collection)
        db.tweets.insert_one(tweet) # uploads tweet into mongodb database, tweets collection

        # prints out tweet in terminal
        try:
            tweet_message = tweet['text']
            logging.critical(tweet_message) 
        except:
            pass

    def on_error(self, status_code):
        if status_code == 420:
            return False



class Stream():
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self, keyword_list):
        self.stream.filter(track=keyword_list)




if __name__ == "__main__":
    listener = Listener()
    
    auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)

    stream.start('qanon')