import pymongo
from sqlalchemy import create_engine
import psycopg2
import time
from datetime import datetime as dt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



# mongo connection
client = pymongo.MongoClient(host="mongodb", port=27017)
db = client.twt
col = db.vac
docs = col.find({})



# postgres connection
ngn = create_engine("postgresql://postgres:1234@postgresdb:5432/twt", echo=True)
ngn.execute("""
            CREATE TABLE IF NOT EXISTS vac (
            twt_id VARCHAR(256),
            twt_dt TIMESTAMP,
            twt_text VARCHAR(500),
            sentiment NUMERIC,
            PRIMARY KEY (twt_id)
);""")



# etl functions
s = SentimentIntensityAnalyzer()


def get_data(doc):
    a = doc["id_str"]
    b = dt.strftime(dt.strptime(doc["created_at"],\
        '%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%dT%H:%M:%S')
    c = doc["text"]
    d = s.polarity_scores(c)["compound"]
    return a, b, c, d


def upload_twt(doc):
    a, b, c, d = get_data(doc)
    query = """
                INSERT INTO vac
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (twt_id)
                DO NOTHING
    ;"""
    ngn.execute(query, (a, b, c, d))
    return None


def full_upload(docs=docs):
    while True:
        for doc in docs:
            try:
                upload_twt(doc)
            except KeyError:
                continue
        time.sleep(5)
    return None



# run etl
if __name__ == "__main__":
    full_upload()
