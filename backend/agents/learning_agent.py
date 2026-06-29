from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.engines.learning_engine import LearningEngine

from backend.models.risk import RiskAssessment
from backend.models.decision_context import DecisionContext
from backend.models.learning import LearningInsight
from backend.planner.register_tools import tool_registry


class LearningAgent(BaseAgent):

    def __init__(self):

        super().__init__("LearningIntelligenceAgent")

        self.engine = tool_registry.get(
            "learning_engine"
        )

    async def execute(

        self,

        context: WorkflowContext

    ) -> WorkflowContext:

        risk: RiskAssessment = context.get(
            "risk"
        )

        decision: DecisionContext = context.get(
            "decision_context"
        )

        if risk is None:

            raise ValueError(
                "Risk assessment not found."
            )

        if decision is None:

            raise ValueError(
                "Decision context not found."
            )

        learning: LearningInsight = self.engine.generate(

            decision,

            risk

        )

        context.set(

            "learning",

            learning

        )

        context.complete_agent(

            self.name

        )

        context.add_log(

            "Learning intelligence generated."

        )

        return context