from pydantic import BaseModel, Field
from typing import List, Dict, Any


class KnowledgePackage(BaseModel):

    query: str

    retrieved_chunks: List[str]

    sources: List[str]

    confidence: float = 0.0

    metadata: Dict[str, Any] = Field(default_factory=dict)