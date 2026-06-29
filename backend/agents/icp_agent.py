import re

from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.engines.icp_engine import ICPEngine
from backend.models.knowledge_package import KnowledgePackage
from backend.models.customer_discovery import CustomerDiscovery


class ICPAgent(BaseAgent):

    def __init__(self):

        super().__init__("ICPAgent")

        self.engine = ICPEngine()

    async def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        knowledge: KnowledgePackage = context.get(
            "knowledge"
        )

        customer: CustomerDiscovery = context.get(
            "customer_discovery"
        )

        if knowledge is None:

            raise ValueError(
                "Knowledge package not found."
            )

        result = self.engine.calculate(
            knowledge
        )

        if customer:

            result.industry = customer.industry

            result.budget_status = customer.budget

            result.timeline_value = customer.timeline

            if customer.decision_makers:

                result.decision_maker = customer.decision_makers[0]

            text = "\n".join(
                knowledge.retrieved_chunks
            )

            match = re.search(
                r"Employees:\s*([\d,]+)",
                text,
                re.IGNORECASE
            )

            if match:

                employees = int(
                    match.group(1).replace(",", "")
                )

                if employees >= 1000:

                    result.company_size = "Enterprise"

                elif employees >= 250:

                    result.company_size = "Mid Market"

                else:

                    result.company_size = "Small Business"

        context.set(
            "icp",
            result
        )

        context.complete_agent(
            self.name
        )

        context.add_log(
            f"ICP Qualification Completed (Score: {result.score})"
        )

        return context