from pydantic import BaseModel, Field


class DecisionContext(BaseModel):

    decision: str

    priority: str

    confidence: float

    business_score: float

    risk_score: float

    approval_level: str

    strategy: str

    triggered_rules: list[dict] = Field(
        default_factory=list
    )

    reasoning: list[str] = Field(
        default_factory=list
    )

    statistics: dict = Field(
        default_factory=dict
    )

    version: str = "2.0"

    agent: str = "DecisionEngine"