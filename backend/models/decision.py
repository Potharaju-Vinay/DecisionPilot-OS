from pydantic import BaseModel, Field
from typing import List


class Decision(BaseModel):

    decision: str

    confidence: float

    reasoning: str

    evidence: List[str] = Field(default_factory=list)

    risks: List[str] = Field(default_factory=list)

    recommendations: List[str] = Field(default_factory=list)

    agent: str = "DecisionAgent"

    status: str = "completed"