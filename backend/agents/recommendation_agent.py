import json
import re

from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.models.decision import Decision
from backend.models.recommendation import Recommendation
from backend.models.action import Action

from backend.prompts.recommendation_prompt import RECOMMENDATION_PROMPT
from backend.services.llm import LLMService
from backend.planner.register_tools import tool_registry

class RecommendationAgent(BaseAgent):

    def __init__(self):

        super().__init__("RecommendationAgent")

        self.llm = tool_registry.get(
            "llm"
        )

    async def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        decision: Decision = context.get("decision")

        customer_discovery = context.get(
            "customer_discovery"
        )

        icp = context.get(
            "icp"
        )

        risk = context.get(
            "risk"
        )

        if decision is None:
            raise ValueError("Decision not found.")

        prompt = RECOMMENDATION_PROMPT.format(
            
            decision=decision.decision,

            reasoning=decision.reasoning,

            risks="\n".join(
                decision.risks
            ),

            opportunity_score=(
                customer_discovery.opportunity_score
                if customer_discovery
                else 0
            ),

            buying_signals=(
                "\n".join(
                    customer_discovery.buying_signals
                )
                if customer_discovery
                else ""
            ),

            pain_points=(
                "\n".join(
                    customer_discovery.pain_points
                )
                if customer_discovery
                else ""
            ),

            business_goals=(
                "\n".join(
                    customer_discovery.business_goals
                )
                if customer_discovery
                else ""
            ),

            icp_score=(
                icp.score
                if icp
                else 0
            ),

            qualified=(
                icp.qualified
                if icp
                else False
            ),

            risk_level=(
                risk.overall_risk
                if risk
                else ""
            )
        )

        response = await self.llm.generate(prompt)

        response = response.strip()

        response = re.sub(r"^```json", "", response)
        response = re.sub(r"^```", "", response)
        response = re.sub(r"```$", "", response)

        response = response.strip()

        match = re.search(r"\{.*\}", response, re.DOTALL)

        if match:
            json_text = match.group(0)
        else:
            json_text = response

        try:

            data = json.loads(json_text)

            actions = []

            for index, item in enumerate(data.get("actions", []), start=1):

                if isinstance(item, dict):

                    actions.append(

                        Action(

                            id=item.get(
                                "id",
                                f"ACT{index:03}"
                            ),

                            description=item.get(
                                "description",
                                ""
                            ),

                            owner=item.get(
                                "owner",
                                item.get(
                                    "assignee",
                                    ""
                                )
                            ),

                            due_date=item.get(
                                "due_date",
                                item.get(
                                    "deadline",
                                    item.get(
                                        "timeline",
                                        ""
                                    )
                                )
                            ),

                            status="Pending"

                        )

                    )

                else:

                    actions.append(

                        Action(

                            id=f"ACT{index:03}",

                            description=str(item),

                            owner="",

                            due_date="",

                            status="Pending"

                        )

                    )

            recommendation = Recommendation(

                priority=data.get(
                    "priority",
                    "Medium"
                ),

                summary=data.get(
                    "summary",
                    ""
                ),

                actions=actions,

                owner=data.get(
                    "owner",
                    ""
                ),

                timeline=data.get(
                    "timeline",
                    ""
                )

            )

        except Exception as e:

            recommendation = Recommendation(

                priority="Medium",

                summary=f"JSON Parsing Failed\n\n{str(e)}",

                actions=[],

                owner="",

                timeline=""

            )

        context.set(
            "recommendation",
            recommendation
        )

        context.complete_agent(
            self.name
        )

        context.add_log(
            "Recommendation generated."
        )

        return context