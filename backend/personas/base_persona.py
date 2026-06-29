from abc import ABC, abstractmethod


class BasePersona(ABC):

    def __init__(self, name: str):

        self.name = name

    @abstractmethod
    def build(self, context):

        pass