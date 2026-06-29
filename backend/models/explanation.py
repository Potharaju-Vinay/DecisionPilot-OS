from typing import List

from pydantic import BaseModel, Field


class Explanation(BaseModel):

    summary: str

    decision: str

    confidence: float

    evidence: List[str] = Field(default_factory=list)

    risks: List[str] = Field(default_factory=list)

    recommendations: List[str] = Field(default_factory=list)

    key_factors: List[str] = Field(default_factory=list)

    explanation: str

    agent: str = "ExplainabilityAgent"

    status: str = "completed"