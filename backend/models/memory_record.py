from pydantic import BaseModel, Field
from typing import Dict, Any
from datetime import datetime


class MemoryRecord(BaseModel):

    id: str

    agent: str

    key: str

    value: Any

    timestamp: datetime = Field(default_factory=datetime.utcnow)

    metadata: Dict[str, Any] = Field(default_factory=dict)