from pydantic import BaseModel
from typing import List


class ICPResult(BaseModel):

    score: float

    qualified: bool

    budget: bool

    authority: bool

    need: bool

    timeline: bool

    industry_fit: bool

    technical_fit: bool

    buying_signals: List[str]

    missing_requirements: List[str]

    reasoning: str

    # New fields for Dashboard

    industry: str = ""

    company_size: str = ""

    budget_status: str = ""

    decision_maker: str = ""

    timeline_value: str = ""