"""Web App
This web app takes in user input (str), looks up that keyword in Twitter and
returns a table with data on tweets about that keyword alongside a sentiment
score.
"""

import subprocess
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import psycopg2


# getting data
NGN = create_engine("postgresql://postgres:1234@postgresdb/twt")


# web app

# get keyword
st.header("Sentiment Search")
st.text_input("Choose a keyword", key="keyword")
kw = st.session_state.keyword

# kick off streamer


# st.write(kw)
QUERY = f"SELECT * FROM vac WHERE search_kw = '{kw}'"
data = NGN.execute(QUERY)
cols = data.keys()
DATA = pd.DataFrame(data, columns=cols)

# display data
if len(DATA):
    st.write(DATA)


# testing
re = subprocess.run("ls -la", capture_output=True, shell=True)
st.write(re.stdout.decode().split("\n"))
