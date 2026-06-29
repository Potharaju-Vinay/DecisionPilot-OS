from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.engines.customer_discovery_engine import CustomerDiscoveryEngine

from backend.models.knowledge_package import KnowledgePackage
from backend.models.customer_discovery import CustomerDiscovery

import json
import re

from backend.prompts.customer_discovery_prompt import CUSTOMER_DISCOVERY_PROMPT
from backend.planner.register_tools import tool_registry


class CustomerDiscoveryAgent(BaseAgent):

    def __init__(self):

        super().__init__("CustomerDiscoveryAgent")

        self.engine = CustomerDiscoveryEngine()

        self.llm = tool_registry.get(
            "llm"
        )

    async def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        knowledge: KnowledgePackage = context.get(
            "knowledge"
        )

        parsed_document = context.get(
            "parsed_document"
        )

        if knowledge is None:

            raise ValueError(
                "Knowledge package not found."
            )

        discovery = CustomerDiscovery()

        try:

            prompt = CUSTOMER_DISCOVERY_PROMPT.format(

                document=parsed_document.content

            )

            response = await self.llm.generate(
                prompt
            )

            print("\n========== LLM RESPONSE ==========\n")

            print(response)

            print("\n=================================\n")

            response = response.strip()

            response = re.sub(
                r"^```json",
                "",
                response
            )

            response = re.sub(
                r"^```",
                "",
                response
            )

            response = re.sub(
                r"```$",
                "",
                response
            )

            response = response.strip()

            response = response.strip()

            response = re.sub(
                r"^```json",
                "",
                response
            )

            response = re.sub(
                r"^```",
                "",
                response
            )

            response = re.sub(
                r"```$",
                "",
                response
            )

            response = response.strip()

            match = re.search(

                r"\{.*\}",

                response,

                re.DOTALL

            )

            json_text = (

                match.group(0)

                if match

                else response

            )

            data = json.loads(
                json_text
            )

            discovery.company = data.get(
                "company",
                ""
            )

            discovery.industry = data.get(
                "industry",
                ""
            )

            discovery.budget = data.get(
                "budget",
                ""
            )

            discovery.timeline = data.get(
                "timeline",
                ""
            )

            discovery.decision_makers = data.get(
                "decision_makers",
                []
            )

            discovery.business_goals = data.get(
                "business_goals",
                []
            ) 

            discovery.pain_points = data.get(
                "pain_points",
                []
            )

            discovery.buying_signals = data.get(
                "buying_signals",
                []
            )

            discovery.objections = data.get(
                "objections",
                []
            )

            discovery.next_best_actions = data.get(
                "next_best_actions",
                []
            )

            discovery.qualification_summary = data.get(
                "qualification_summary",
                ""
            )

            discovery.opportunity_score = min(

                100,

                len(discovery.buying_signals) * 15 +

                len(discovery.business_goals) * 10 +

                len(discovery.decision_makers) * 10

            )

        except Exception as e:

            print(e)

            discovery = self.engine.analyze(
                knowledge
            )

        print("\n========== CUSTOMER DISCOVERY ==========")
        print(discovery)
        print("========================================")

        context.set(
            "customer_discovery",
            discovery
        )

        print("\n===== CUSTOMER DISCOVERY =====")
        print("Goals:", discovery.business_goals)
        print("Signals:", discovery.buying_signals)
        print("==============================")

        context.complete_agent(
            self.name
        )

        context.add_log(

            f"Customer Discovery completed. "

            f"Opportunity Score: {discovery.opportunity_score}"

        )

        return context