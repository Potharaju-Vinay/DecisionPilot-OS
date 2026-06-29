from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.engines.analytics_engine import AnalyticsEngine

from backend.models.analytics import Analytics
from backend.models.knowledge_package import KnowledgePackage
from backend.models.risk import RiskAssessment
from backend.models.decision_context import DecisionContext
from backend.models.recommendation import Recommendation
from backend.models.explanation import Explanation
from backend.planner.register_tools import tool_registry

class AnalyticsAgent(BaseAgent):

    def __init__(self):

        super().__init__("AnalyticsAgent")

        self.engine = tool_registry.get(
            "analytics_engine"
        )

    async def execute(

        self,

        context: WorkflowContext

    ) -> WorkflowContext:

        knowledge: KnowledgePackage = context.get(
            "knowledge"
        )

        risk: RiskAssessment = context.get(
            "risk"
        )

        decision: DecisionContext = context.get(
            "decision_context"
        )

        recommendation: Recommendation = context.get(
            "recommendation"
        )

        explanation: Explanation = context.get(
            "explanation"
        )

        metrics = context.metrics

        if knowledge is None:

            raise ValueError(
                "Knowledge package not found."
            )

        if risk is None:

            raise ValueError(
                "Risk assessment not found."
            )

        if decision is None:

            raise ValueError(
                "Decision context not found."
            )

        if recommendation is None:

            raise ValueError(
                "Recommendation not found."
            )

        if explanation is None:

            raise ValueError(
                "Explanation not found."
            )

        analytics: Analytics = self.engine.calculate(

            knowledge,

            risk,

            decision,

            recommendation,

            explanation,

            metrics

        )

        context.set(

            "analytics",

            analytics

        )

        context.complete_agent(

            self.name

        )

        context.add_log(

            "Enterprise analytics generated."

        )

        return context