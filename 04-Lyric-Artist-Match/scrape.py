# data scraping
import requests
import re
from bs4 import BeautifulSoup

# functions
import numpy as np
import pandas as pd
import time


''' SCRAPE ARTIST SONGS '''

def artist_url(artist):
    ''' Create artist page url for a given artist '''

    artist = artist.lower().replace(' ','+')
    return f'https://www.lyrics.com/artist/{artist}'


def artist_html(artist_url):
    ''' Scrape exhaustive list of songs of a given artist '''

    url_hash = hash(artist_url)
    file_name = f'data/{url_hash}.txt'

    try:
        f = open(file_name,'r')
        artist_html = f.read()

    
    except:
        artist_html = requests.get(artist_url).text
        
        f = open(file_name,'w')
        f.write(artist_html)
        f.close()

    return artist_html


def parse_html(artist_html):
    ''' Parse html into list of songs given an artist html '''

    soup = BeautifulSoup(artist_html,'html.parser')
    song_html = soup.find_all('td', class_='tal')

    return song_html


def scrape_artist(artist):
    ''' Scrape list of songs for a given artist '''

    var = artist_url(artist)
    var2 = artist_html(var)
    var3 = parse_html(var2)

    artist_name = [ artist for song in var3 ]
    artist_songs = [ song.a.text for song in var3 ]
    artist_links = [ 'https://www.lyrics.com' + song.a['href'] for song in var3 ]
    result = np.column_stack((artist_name, artist_songs, artist_links))

    return result



""" SCRAPE LYRICS """

def scrape_lyrics(songs, n):

    """ This function scrapes lyrics for each song of a given list of songs (urls) """

    song_links = songs[:n,2]
    lyrics = []
    for song_link in song_links:
        
        file_name = 'data/' + str(hash(song_link)) + '.txt'

        try:
            f = open(file_name,'r')
            html_lyric = f.read()


        except:
            time.sleep(3)
            html_lyric = requests.get(song_link).text
            f = open(file_name,'w')
            f.write(html_lyric)
            f.close()

        soup_lyric = BeautifulSoup(html_lyric, 'html.parser')
        lyric = soup_lyric.pre.text
        lyrics.append(lyric)

    lyrics = np.column_stack((songs[:n,:], lyrics))

    lyrics_df = pd.DataFrame(lyrics)
    lyrics_df.to_csv('data/lyrics_df.csv')

    return lyrics