from datetime import datetime

from backend.agents.base_agent import BaseAgent

from backend.execution.workflow_context import WorkflowContext

from backend.models.decision_audit import DecisionAudit


class AuditAgent(BaseAgent):

    def __init__(self):

        super().__init__("AuditAgent")

    async def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        knowledge = context.get("knowledge")

        decision = context.get("decision")

        risk = context.get("risk")

        rules = context.get(
            "business_rules",
            {}
        )

        audit = DecisionAudit(

            timestamp=datetime.now(),

            query=context.get("query"),

            document=context.get(
                "parsed_document"
            ).source,

            retrieved_chunks=len(
                knowledge.retrieved_chunks
            ),

            retrieved_sources=len(
                set(
                    knowledge.sources
                )
            ),

            retrieval_confidence=knowledge.confidence,

            business_score=rules.get(
                "score",
                0
            ),

            business_rules=rules.get(
                "reasons",
                []
            ),

            risk_score=risk.overall_score,

            risk_level=risk.overall_risk,

            decision=decision.decision,

            decision_confidence=decision.confidence,

            execution_time=sum(
                context.metrics.values()
            ),

            completed_agents=context.completed_agents,

            workflow_logs=context.logs

        )

        context.set(
            "audit",
            audit
        )

        context.complete_agent(
            self.name
        )

        context.add_log(
            "Decision audit generated."
        )

        return context