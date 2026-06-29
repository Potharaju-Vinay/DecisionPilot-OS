from pydantic import BaseModel
from typing import List


class CustomerDiscovery(BaseModel):

    company: str = ""

    industry: str = ""

    budget: str = ""

    timeline: str = ""

    decision_makers: List[str] = []

    pain_points: List[str] = []

    business_goals: List[str] = []

    buying_signals: List[str] = []

    objections: List[str] = []

    next_best_actions: List[str] = []

    qualification_summary: str = ""

    opportunity_score: float = 0