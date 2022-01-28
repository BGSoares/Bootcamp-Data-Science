import pymongo
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import time
import logging
import numpy as np

time.sleep(5)


# connecting to mongodb
client = pymongo.MongoClient(host="mongodb", port=27017)
db = client.twitter
docs = db.tweets.find()

# setting up temp dataframe
column_names = ['user', 'message', 'sentiment']
df = pd.DataFrame(columns=column_names)

# connecting to postgres db
pg = create_engine('postgresql://postgres:1234@postgresdb:5432/twitter', echo=True)

# creating table
pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    id VARCHAR(256),
    timestamp DATETIME,
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

# append each tweet (selected variables) in mongodb to the dataframe
while True:
    for doc in docs:
        try:
            tweet_id = doc['id_str'] # check if this exists
            # tweet_user = doc['user']['name']
            tweet_timestamp = doc['created_at']
            tweet_message = doc['text']
            tweet_sentiment = 1
            query = "SELECT id FROM tweets"
            tweets_already_uploaded = list(pg.execute(query))
            if tweet_id not in tweets_already_uploaded:
                query = "INSERT INTO tweets VALUES (%s, %s, %s);"
                pg.execute(query, (tweet_id, tweet_message, tweet_sentiment))
        except:
            pass