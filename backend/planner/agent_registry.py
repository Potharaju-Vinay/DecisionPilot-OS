from dataclasses import dataclass
from typing import List


@dataclass
class AgentMetadata:

    name: str

    description: str

    capabilities: List[str]

    inputs: List[str]

    outputs: List[str]

    tools: List[str]

    dependencies: List[str]


class AgentRegistry:

    def __init__(self):

        self._agents = {}

        self._metadata = {}

    def register(

        self,

        agent,

        metadata: AgentMetadata

    ):

        self._agents[agent.name] = agent

        self._metadata[agent.name] = metadata

    def get(

        self,

        name

    ):

        return self._agents.get(name)

    def metadata(

        self,

        name

    ):

        return self._metadata.get(name)

    def get_agents(

        self

    ):

        return list(

            self._agents.values()

        )

    def all_metadata(

        self

    ):

        return list(

            self._metadata.values()

        )