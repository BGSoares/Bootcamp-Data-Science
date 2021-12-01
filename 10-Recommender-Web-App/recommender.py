
import random

MOVIES = [
    "Bruised",
    "Red Notice",
    "Love Hard",
    "The Other Son",
    "Into the Wild"
]

def recommend():
    return random.choice(MOVIES)

print(recommend())