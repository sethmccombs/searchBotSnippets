from flask import Flask
from serpapi import GoogleSearch
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route('/')

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
    app.run(debug = True)
    print("What should I search for?")
    # search_term = input("Search Term: ")
    # print(search_google(search_term))
