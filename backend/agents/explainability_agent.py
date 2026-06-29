import json
import re

from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.models.decision import Decision
from backend.models.explanation import Explanation

from backend.prompts.explainability_prompt import EXPLAINABILITY_PROMPT
from backend.services.llm import LLMService
from backend.planner.register_tools import tool_registry


class ExplainabilityAgent(BaseAgent):

    def __init__(self):

        super().__init__("ExplainabilityAgent")

        self.llm = tool_registry.get(
            "llm"
        )
    async def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        decision: Decision = context.get("decision")

        risk = context.get(
            "risk"
        )

        customer_discovery = context.get(
            "customer_discovery"
        )

        icp = context.get(
            "icp"
        )

        knowledge_graph = context.get(
            "knowledge_graph"
        )

        rule_result = context.get(
            "rule_result"
        )

        recommendation = context.get(
            "recommendation"
        )

        if decision is None:
            raise ValueError("Decision not found.")

        prompt = EXPLAINABILITY_PROMPT.format(

            decision=decision.decision,

            reasoning=decision.reasoning,

            evidence="\n".join(decision.evidence),

            risks="\n".join(decision.risks),

            risk_level=(
                risk.overall_risk
                if risk
                else ""
            ),

            risk_summary=(
                risk.summary
                if risk
                else ""
            ),

            opportunity_score=(
                customer_discovery.opportunity_score
                if customer_discovery
                else 0
            ),

            business_goals=(
                "\n".join(
                    customer_discovery.business_goals
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

            buying_signals=(
                "\n".join(
                    customer_discovery.buying_signals
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

            graph_nodes=(
                len(knowledge_graph.nodes)
                if knowledge_graph
                else 0
            ),

            graph_edges=(
                len(knowledge_graph.edges)
                if knowledge_graph
                else 0
            ),

            matched_rules=(
                len(
                    rule_result.get(
                        "triggered_rules",
                        []
                    )
                )
                if rule_result
                else 0
            ),

            recommendations="\n".join(
                decision.recommendations
            )
        )

        response = await self.llm.generate(prompt)

        response = response.strip()

        response = re.sub(r"^```json", "", response)
        response = re.sub(r"^```", "", response)
        response = re.sub(r"```$", "", response)

        response = response.strip()

        match = re.search(
            r"\{.*\}",
            response,
            re.DOTALL
        )

        if match:

            json_text = match.group(0)

        else:

            json_text = response

        try:

            data = json.loads(json_text)

            summary = data.get(
                "summary",
                ""
            )

            details = data.get(
                "explanation",
                ""
            )

            if isinstance(details, dict):

                details = "\n\n".join(

                    f"{key.replace('_', ' ').title()}:\n{value}"

                    for key, value in details.items()

                )

            explanation = Explanation(

                summary=summary,

                explanation=details,

                decision=decision.decision,

                confidence=decision.confidence,

                evidence=decision.evidence,

                risks=decision.risks,

                recommendations=decision.recommendations

            )

        except Exception:

            explanation = Explanation(

                summary="",

                explanation=response,

                decision=decision.decision,

                confidence=decision.confidence,

                evidence=decision.evidence,

                risks=decision.risks,

                recommendations=decision.recommendations

            )

        context.set(
            "explanation",
            explanation
        )

        context.complete_agent(
            self.name
        )

        context.add_log(
            "Explanation generated."
        )

        return context