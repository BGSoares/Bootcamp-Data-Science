import requests
import re
from bs4 import BeautifulSoup
import numpy as np
import tqdm
import pandas as pd
import os.path

def scrape_songs(artist):
    
    site = 'https://www.lyrics.com/artist/'
    artist_ = artist.replace(' ','-')
    url_artist = site + artist
    
    html_artist = requests.get(url_artist).text

    
    soup = BeautifulSoup(html_artist, features='html.parser')
    songs = soup.find_all('td', class_='tal')
    artist_songs = [ song.a.text for song in songs ]
    artist_links = [ url_artist + song.a['href'] for song in songs ]
    result = np.column_stack((artist_songs, artist_links))
    return result

artist1 = 'dua lipa'

artist1_songs = scrape_songs(artist1)

def scrape_lyrics(songs, n):
    song_links = songs[:n,1]
    lyrics = []


    try open()

    for song in song_links:

        try f = open

        result = requests.get(song)
        soup_lyric = BeautifulSoup(result.text)
        lyric = soup_lyric.pre.text
        lyrics.append(lyric)
    return lyrics

