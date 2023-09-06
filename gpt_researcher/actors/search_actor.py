# search_actor.py

from tavily_python import tavily

class SearchActor():
    def __init__(self):
        self.api_key = "YOUR_API_KEY"

    def search(self, query):
        client = tavily.Client(self.api_key)
        res = client.advanced_search(query)
        print(res)
        return res
