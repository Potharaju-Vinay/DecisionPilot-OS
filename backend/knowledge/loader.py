from backend.services.input_engine import UniversalInputEngine


class KnowledgeLoader:

    def __init__(self):

        self.engine = UniversalInputEngine()

    def load(self, source: str):

        return self.engine.parse(source)