
from flask import Flask, render_template, request
from recommender import recommend

app = Flask("Brunnos Movie Recommender")

# connects the URL "/" to the function hello()
@app.route('/') # < - - a URL for a web page
def hello_world():
    return render_template('hello.html')

@app.route('/reco/')
def recommendation():
    genre = request.args['genre']
    movie = recommend(genre)
    return render_template("result.html", movie=movie)

if __name__ == "__main__":
    app.run(debug=True)
