"""Extract-Transform-Load module
This module extracts data from the MongoDB database, processes it by taking only
interesting datapoints for each tweet, calculating a sentiment score, and uploading
the above into a PostgreSQL DB.
"""


from datetime import datetime as dt
import pymongo
from sqlalchemy import create_engine
import psycopg2
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# mongo connection
client = pymongo.MongoClient(host="mongodb", port=27017)
db = client.twt
COLLECTION = db.vac.find({})


# postgres connection
ngn = create_engine("postgresql://postgres:1234@postgresdb:5432/twt", echo=True)
ngn.execute("""
            CREATE TABLE IF NOT EXISTS vac (
            twt_id VARCHAR(256),
            twt_dt TIMESTAMP,
            twt_text VARCHAR(500),
            sentiment FLOAT,
            PRIMARY KEY (twt_id)
);""")



# etl functions
s = SentimentIntensityAnalyzer()


def get_data(doc):
    """Get interesting data from tweets.

    Args:
        doc (MongoDB document): Each MongoDB document is similar to a row in a table.

    Returns:
        twt_id (string): Tweet ID as assigned by Twitter.
        twt_ts (string): Tweet creating timestamp.
        twt_txt (string): Tweet text.
        sentiment (float): Sentiment analysis score. Vader compound score used.
    """
    twt_id = doc["id_str"]

    twt_ts = dt.strftime(dt.strptime(doc["created_at"],\
        '%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%dT%H:%M:%S')

    twt_txt = doc["text"]

    sentiment = s.polarity_scores(twt_txt)["compound"]

    return (twt_id, twt_ts, twt_txt, sentiment)


def upload_twt(doc):
    """Upload a single Tweet as a row in PostgreSQL DB.

    Args:
        doc (MongoDB document): Each MongoDB document is similar to a row in a table.

    Returns:
        (None): Uploads a single MongoDB document as a row into PostgreSQL DB. Returns nothing.
    """
    query = """
            INSERT INTO vac
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (twt_id)
            DO NOTHING
            ;"""
    ngn.execute(query, get_data(doc))


def full_upload(docs=COLLECTION):
    """Uploads each MongoDB document as a row into the PostgreSQL DB.

    Args:
        docs (collection, optional): MongoDB object containing collections. Defaults to docs.

    Returns:
        (None): Uploads MongoDB documents as rows into PostgresSQL DB. Returns nothing.
    """
    for doc in docs:
        try:
            upload_twt(doc)
        except KeyError:
            print('key error')
            continue



# run etl
if __name__ == "__main__":
    while True:
        COLLECTION = db.vac.find({})
        full_upload(docs=COLLECTION)
