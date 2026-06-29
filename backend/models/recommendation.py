from pydantic import BaseModel, Field
from typing import List

from backend.models.action import Action


class Recommendation(BaseModel):

    priority: str

    summary: str

    actions: List[Action] = Field(default_factory=list)

    owner: str

    timeline: str

    agent: str = "RecommendationAgent"

    status: str = "completed"