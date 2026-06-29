from pydantic import BaseModel, Field
from typing import Dict, Any


class DocumentChunk(BaseModel):

    chunk_id: str

    document_id: str

    chunk_index: int

    content: str

    metadata: Dict[str, Any] = Field(default_factory=dict)