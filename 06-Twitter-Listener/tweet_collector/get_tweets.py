import tweepy
import credentials
import pymongo


class Listener(tweepy.StreamListener):

    def on_data(self, raw_data): 

        self.process_data(raw_data)
        return True

    def process_data(self, raw_data):
        print(raw_data)

    def on_error(self, status_code):
        if status_code == 420:
            return False

class Stream():
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self, keyword_list):
        self.stream.filter(track=keyword_list)

def upload_to_mongodb(tweet):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.twitterdb
    db.twitterdb_data.insert(tweet)

if __name__ == "__main__":
    listener = Listener()
    
    auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listener)

    upload_to_mongodb(stream.start(['bolsonaro']))