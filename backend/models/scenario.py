from pydantic import BaseModel, Field


class Scenario(BaseModel):

    scenario_name: str

    description: str

    changes: dict

    original_business_score: float

    simulated_business_score: float

    original_risk_score: float

    simulated_risk_score: float

    original_decision: str

    simulated_decision: str

    impact: str

    confidence: float


class ScenarioResult(BaseModel):

    scenarios: list[Scenario]

    total_scenarios: int

    generated_by: str = "Scenario Intelligence Engine"

    version: str = "1.0"

    statistics: dict = Field(
        default_factory=dict
    )

    agent: str = "ScenarioIntelligenceAgent"

    status: str = "completed"