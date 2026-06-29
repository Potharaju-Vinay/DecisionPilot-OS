from backend.knowledge.vector_store import VectorStore


class KnowledgeRetriever:

    def __init__(self):

        self.vector_store = VectorStore()

    def search(
        self,
        query: str
    ):

        return self.vector_store.search(query)