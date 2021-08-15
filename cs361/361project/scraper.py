from flask import Flask, render_template
from wineries import states
# import scraper

app = Flask(__name__)


# Connects app to home page
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", states=states)


# May implement this later so that each state has it's own separate page for wineries

# @app.route("/<state>")
# def states(state):
#     return render_template("states.html")


@app.route("/<name>")
def winery(name):
    return render_template("winery.html", template_name=name, states=states)

