from pydantic import BaseModel, Field
from typing import Dict, Any, Optional


class ParsedDocument(BaseModel):
    source: str
    file_type: str
    content: str

    title: Optional[str] = None

    metadata: Dict[str, Any] = Field(default_factory=dict)