
import random
import json

f = open("data.json")
MOVIES = json.load(f)

def recommend(genre):
    movie = MOVIES.get(genre, MOVIES["comedy"])
    return random.choice(movie)

if __name__ == "__main__":
    print(recommend("comedy"))
