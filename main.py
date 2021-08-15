from flask import Flask, request, jsonify
from serpapi import GoogleSearch
from flask_restful import Resource, Api

app = Flask(__name__)


@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


def hello_world():
   return('Hello World')

def search_google(query_term):

    params = {
        "api_key": "*",
        "engine": "google",
        "q": "query_term",
        "location": "Austin, Texas, United States",
        "google_domain": "google.com",
        "gl": "us",
        "hl": "en"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
    # app.run(debug = True)
    print("What should I search for?")
    # search_term = input("Search Term: ")
    # print(search_google(search_term))
