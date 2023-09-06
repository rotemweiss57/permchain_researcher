from .actors.search_actor import SearchActor
from .actors.writer_actor import WriterActor

from permchain.connection_inmemory import InMemoryPubSubConnection
from permchain.pubsub import PubSub
from permchain.topic import Topic


class Researcher:
    def __init__(self, query):
        self.query = query
        self.search_actor_instance = SearchActor()
        self.writer_actor_instance = WriterActor()

    def run(self):
        # The research inbox
        research_inbox = Topic("research")

        search_actor = (
            Topic.IN.subscribe()
            | self.search_actor_instance.search
            | research_inbox.publish()
        )

        write_actor = (
            research_inbox.subscribe()
            | self.writer_actor_instance.write
            | Topic.OUT.publish()
        )

        researcher = PubSub(
            processes=(search_actor, write_actor),
            connection=InMemoryPubSubConnection(),
        )

        res = researcher.invoke(self.query)
        return res
