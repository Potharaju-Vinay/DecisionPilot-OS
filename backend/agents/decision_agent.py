import json
import re

from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.engines.decision_engine import DecisionEngine

from backend.models.knowledge_package import KnowledgePackage
from backend.models.risk import RiskAssessment
from backend.models.decision import Decision
from backend.models.decision_context import DecisionContext

from backend.prompts.decision_prompt import DECISION_PROMPT
from backend.services.llm import LLMService
from backend.planner.register_tools import tool_registry

class DecisionAgent(BaseAgent):

    def __init__(self):

        super().__init__("DecisionAgent")

        self.engine = DecisionEngine()

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

        risk: RiskAssessment = context.get(
            "risk"
        )

        knowledge_graph = context.get(
            "knowledge_graph"
        )

        customer_discovery = context.get(
            "customer_discovery"
        )

        icp = context.get(
            "icp"
        )

        rule_result = context.get(
            "rule_result",
            {}
        )

        decision_context: DecisionContext = self.engine.evaluate(

            knowledge,

            risk,

            rule_result

        )

        prompt = DECISION_PROMPT.format(

            query=context.get("query"),

            business_score=decision_context.business_score,

            business_reasons="\n".join(

                decision_context.reasoning

            ),

            risk_level=risk.overall_risk,

            risk_score=decision_context.risk_score,

            risk_summary=risk.summary,

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

            evidence="\n".join(

                knowledge.retrieved_chunks

            )

        )

        response = await self.llm.generate(
            prompt
        )

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

        try:

            data = json.loads(
                json_text
            )

            decision = Decision(

                decision=decision_context.decision,

                confidence=decision_context.confidence,

                reasoning=data.get(
                    "reasoning",
                    ""
                ),

                evidence=knowledge.retrieved_chunks,

                risks=data.get(
                    "risks",
                    []
                ),

                recommendations=data.get(
                    "recommendations",
                    []
                )

            )

        except Exception:

            decision = Decision(

                decision=decision_context.decision,

                confidence=decision_context.confidence,

                reasoning=response,

                evidence=knowledge.retrieved_chunks,

                risks=[],

                recommendations=[]

            )

        context.set(

            "decision",

            decision

        )

        context.set(

            "decision_context",

            decision_context

        )

        context.complete_agent(

            self.name

        )

        context.add_log(

            "Decision generated."

        )

        return context