from pydantic import BaseModel, Field


class RiskAssessment(BaseModel):

    overall_risk: str

    overall_score: float

    business_risk: float

    financial_risk: float

    operational_risk: float

    technical_risk: float

    compliance_risk: float

    business_score: float

    approval_score: float

    compliance_score: float

    rule_result: dict = Field(default_factory=dict)

    triggered_rules: list[dict] = Field(
        default_factory=list
    )

    risk_factors: list[str] = Field(
        default_factory=list
    )

    recommendations: list[str] = Field(
        default_factory=list
    )

    statistics: dict = Field(
        default_factory=dict
    )

    summary: str

    confidence: float = 1.0

    version: str = "2.0"

    agent: str = "RiskAgent"

    status: str = "completed"