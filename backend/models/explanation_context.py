from pydantic import BaseModel, Field


class ExplanationContext(BaseModel):

    decision: str

    confidence: float

    business_score: float

    risk_score: float

    approval_level: str

    evidence_strength: str

    decision_path: list[str]

    evidence: list[str]

    triggered_rules: list[dict]

    key_factors: list[str]

    statistics: dict = Field(
        default_factory=dict
    )