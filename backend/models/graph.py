from pydantic import BaseModel
from typing import List


class GraphNode(BaseModel):

    id: str

    type: str

    value: str


class GraphEdge(BaseModel):

    source: str

    target: str

    relation: str


class KnowledgeGraph(BaseModel):

    nodes: List[GraphNode]

    edges: List[GraphEdge]