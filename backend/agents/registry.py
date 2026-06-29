from dataclasses import dataclass
from typing import Dict, List


@dataclass
class AgentMetadata:

    name: str

    description: str

    capabilities: List[str]

    inputs: List[str]

    outputs: List[str]

    tools: List[str]


class AgentRegistry:

    def __init__(self):

        self._agents: Dict[str, object] = {}

        self._metadata: Dict[str, AgentMetadata] = {}

    def register(

        self,

        agent,

        metadata: AgentMetadata

    ):

        self._agents[metadata.name] = agent

        self._metadata[metadata.name] = metadata

    def get(

        self,

        name: str

    ):

        return self._agents.get(name)

    def metadata(

        self,

        name: str

    ):

        return self._metadata.get(name)

    def all_agents(self):

        return self._agents

    def all_metadata(self):

        return self._metadata

    def clear(self):

        self._agents.clear()

        self._metadata.clear()

    def count(self):

        return len(self._agents)