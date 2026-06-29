from pydantic import BaseModel, Field


class RecommendationContext(BaseModel):

    priority: str

    business_impact: str

    urgency: str

    owner: str

    timeline: str

    estimated_roi: str

    decision_category: str

    next_actions: list[str]

    statistics: dict = Field(
        default_factory=dict
    )