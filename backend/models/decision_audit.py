from datetime import datetime

from pydantic import BaseModel


class DecisionAudit(BaseModel):

    timestamp: datetime

    query: str

    document: str

    retrieved_chunks: int

    retrieved_sources: int

    retrieval_confidence: float

    business_score: float

    business_rules: list[str]

    risk_score: float

    risk_level: str

    decision: str

    decision_confidence: float

    execution_time: float

    completed_agents: list[str]

    workflow_logs: list[str]