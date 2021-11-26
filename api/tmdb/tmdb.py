import os
import json
import requests
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")


class TMDB(object):
    BASE = ""
    URLS = {"search_movie": "/search/movie"}
    context = {"api_key": API_KEY}

    def __init__(self) -> None:
        self.base_url = "https://api.themoviedb.org/3"

    def get_results(self, endpoint) -> list:
        data = requests.get(self.base_url + self.URLS[endpoint], self.context).json()
        return data["results"]

    def search_movie_by_name(self, query) -> list:
        self.context["query"] = query
        return self.get_results("search_movie")

    def get_similar_titles(self, query) -> list:
        result = []
        for el in self.search_movie_by_name(query):
            result.append(el["original_title"])
        return result


# engine = TMDB()
# movies = engine.search_movie_by_name("matrix")
# titles = engine.get_similar_titles("matrix")
# pprint(titles)
