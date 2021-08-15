from serpapi import GoogleSearch
from flask import Flask, request, jsonify
import scraper

app = Flask(__name__)


@app.route('/shop-search/<query_term>', methods=["GET"])
def search_google(query_term):
    params = {
        "api_key": "3beeda75a5aa8dd1b627d59abb70eaca6a523789554cdb6feed337db7b892b80",
        "engine": "google",
        "q": query_term,
        "tbm": "shop",
        "location": "Portland, Oregon, United States",
        "google_domain": "google.com",
        "gl": "us",
        "hl": "en"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return jsonify(results)


# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
    print("What should I search for?")
    search_term = input("Search Term: ")
    print(search_google(search_term))
