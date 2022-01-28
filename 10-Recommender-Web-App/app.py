
from flask import Flask, render_template, request, jsonify
from recommender import recommend, MOVIES
import random

app = Flask("Brunnos Movie Recommender")

# connects the URL "/" to the function hello()
@app.route("/") # < - - a URL for a web page
def index_page():
    return render_template("index.html")


@app.route("/reco/")
def recommendation():
    genre = request.args["genre"]
    movie = recommend(genre)
    return render_template("result.html", movie=movie)


@app.route("/api/all/")
def api_all_movies():
    return jsonify(MOVIES)



if __name__ == "__main__":
    app.run(debug=True)
