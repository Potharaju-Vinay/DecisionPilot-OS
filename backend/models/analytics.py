from pydantic import BaseModel, Field


class Analytics(BaseModel):

    business_score: float

    risk_score: float

    decision_confidence: float

    knowledge_confidence: float

    ai_confidence: float

    decision_quality_index: float

    business_readiness: float

    system_reliability: float

    evidence_strength: float

    explainability_score: float

    recommendation_quality: float

    workflow_efficiency: float

    rule_coverage: float

    triggered_rules: int

    total_processing_time_ms: float

    engine_processing_time_ms: float

    ai_processing_time_ms: float

    overall_health: str

    # ADD THESE ↓↓↓
    workflow_time: float = 0

    documents_processed: int = 1

    success_rate: int = 100
    # ↑↑↑

    statistics: dict = Field(default_factory=dict)

    version: str = "4.0"

    agent: str = "AnalyticsAgent"

    status: str = "completed"