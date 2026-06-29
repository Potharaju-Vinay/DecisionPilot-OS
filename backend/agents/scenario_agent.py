from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.engines.scenario_engine import ScenarioEngine

from backend.models.knowledge_package import KnowledgePackage
from backend.models.risk import RiskAssessment
from backend.models.decision_context import DecisionContext
from backend.models.scenario import ScenarioResult
from backend.planner.register_tools import tool_registry


class ScenarioAgent(BaseAgent):

    def __init__(self):

        super().__init__("ScenarioAgent")

        self.engine = tool_registry.get(
            "scenario_engine"
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

        result: ScenarioResult = self.engine.generate(

            knowledge=knowledge,

            current_rule_result=risk.rule_result,

            current_decision=decision.decision

        )

        context.set(

            "scenario_result",

            result

        )

        context.complete_agent(

            self.name

        )

        context.add_log(

            f"{result.total_scenarios} scenarios generated."

        )

        return context