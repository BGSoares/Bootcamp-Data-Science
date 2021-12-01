
from flask import Flask
from flask import render_template
from recommender import recommend

app = Flask("Brunnos Movie Recommender")

# connects the URL "/" to the function hello()
@app.route('/') # < - - a URL for a web page
def hello_world():
    return render_template('hello.html')

@app.route('/reco')
def recommendation():
    text = "Your movie recommendation is: " + recommend()
    return text

if __name__ == "__main__":
    app.run(debug=True)
