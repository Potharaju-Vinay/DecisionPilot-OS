from pydantic import BaseModel, Field


class LearningInsight(BaseModel):

    total_decisions: int

    approval_rate: float

    manual_review_rate: float

    rejection_rate: float

    average_business_score: float

    average_risk_score: float

    most_triggered_rule: str

    learning_summary: str

    improvement_recommendation: str

    statistics: dict = Field(
        default_factory=dict
    )

    version: str = "1.0"

    agent: str = "LearningIntelligenceAgent"

    status: str = "completed"