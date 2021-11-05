import requests
from sqlalchemy import create_engine
import psycopg2
import time
import logging

WEBHOOK_URL = "https://hooks.slack.com/services/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"

time.sleep(5)

for i in range(5):
    pg = create_engine('postgresql://postgres:1234@postgresdb:5432/twitter')
    
    query = '''
        SELECT * FROM tweets ORDER BY id DESC LIMIT 1;
    '''
    last_tweet = list(pg.execute(query))

    # logging.critical(len(last_tweet))

    last_tweet_message = last_tweet[0][1]
    last_tweet_sentiment = last_tweet[0][2]
    
    slack_post_content = f"Tweet: {last_tweet_message}. Sentiment: {last_tweet_sentiment}."
    slack_post = {"text":slack_post_content}

    # logging.critical(last_tweet)
    response = requests.post(url=WEBHOOK_URL, json=slack_post)
    # logging.critical(response.content)
    time.sleep(5)