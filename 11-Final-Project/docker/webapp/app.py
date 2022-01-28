"""Web App
This web app takes in user input (str), looks up that keyword in Twitter and
returns a table with data on tweets about that keyword alongside a sentiment
score.
"""

import os
import subprocess
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from matplotlib import pyplot as plt


# getting data
NGN = create_engine("postgresql://postgres:1234@postgresdb/twt")
try:
    os.remove("/app/todo/todo.txt")
except FileNotFoundError:
    pass

# web app

# get keyword
st.header("Sentiment Meter")
# st.text_input("Type a keyword", key="keyword")
# kw = st.session_state.keyword

# kick off streamer


# st.write(kw)
# QUERY =  """SELECT twt_dt,
#                    sentiment,
#                    AVG(sentiment)
#                    OVER(ORDER BY twt_dt ROWS BETWEEN 1000 PRECEDING AND CURRENT ROW)
#                    AS moving_average
#             FROM vac;
#          """

         
st.write("Graph 1: Tweet Count")
QUERY1 = """SELECT COUNT(sentiment),
                   to_timestamp(floor((extract('epoch' from twt_dt) / 600)) * 600)
                   AT TIME ZONE 'UTC-1' AS t
            FROM vac
            GROUP BY t;
        """
data = NGN.execute(QUERY1)
DATA1 = pd.DataFrame(data, columns=data.keys()).set_index('t')
st.line_chart(DATA1)


st.write("Graph 2: Sentiment Trend")
QUERY2 = """SELECT AVG(sentiment),
                   to_timestamp(floor((extract('epoch' from twt_dt) / 600)) * 600)
                   AT TIME ZONE 'UTC-1' AS t
            FROM vac GROUP BY t;
        """
data = NGN.execute(QUERY2)
DATA2 = pd.DataFrame(data, columns=data.keys()).set_index('t')
st.line_chart(DATA2)


st.write("Sample Tweets")
QUERY3 = """SELECT twt_text,
                   sentiment
            FROM vac
            ORDER BY twt_dt DESC
            LIMIT 5;
        """
data = NGN.execute(QUERY3)
DATA3 = pd.DataFrame(data, columns=data.keys())
st.table(DATA3)
