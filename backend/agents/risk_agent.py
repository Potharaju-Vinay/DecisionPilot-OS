from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.engines.risk_engine import RiskEngine

from backend.models.knowledge_package import KnowledgePackage
from backend.planner.register_tools import tool_registry


class RiskAgent(BaseAgent):

    def __init__(self):

        super().__init__("RiskAgent")

        

        self.engine = tool_registry.get(
            "risk_engine"
        )

    async def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        knowledge: KnowledgePackage = context.get(
            "knowledge"
        )

        if knowledge is None:

            raise ValueError(
                "Knowledge package not found."
            )

        result = self.engine.calculate(
            knowledge
        )

        context.set(
            "rule_result",
            result["rule_result"]
        )

        context.set(
            "risk",
            result["risk"]
        )

        context.complete_agent(
            self.name
        )

        context.add_log(
            "Risk assessment completed."
        )

        return context