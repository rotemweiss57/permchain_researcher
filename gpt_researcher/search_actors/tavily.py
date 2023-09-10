from tavily import Client
from langchain.schema.runnable import RunnableLambda


class TavilySearchActor:
    def __init__(self):
        self.api_key = "4a4b0c9f18f14cd0b1c02e23816b8fe9"

    @property
    def runnable(self):
        client = Client(self.api_key)
        return RunnableLambda(client.advanced_search) | {"results": lambda x: x["results"]}
