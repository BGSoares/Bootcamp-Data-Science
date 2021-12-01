
import random

MOVIES = {
    'action':[
        'Die Hard',
        'Bruised',
        'Red Notice',
        'John Wick'
    ],
    'romance':[
        'Titanic',
        'Love Hard'
    ],
    'comedy':[
        'Bad Santa',
        'Kevin Alone at Home',
        'Christmas Princess IV'
    ],
    'drama':[
        'Into the Wild',
        'The Other Son'
    ]
}

def recommend(genre):
    movie = MOVIES.get(genre, MOVIES['comedy'])
    return random.choice(movie)

if __name__ == '__main__':
    print(recommend('comedy'))
