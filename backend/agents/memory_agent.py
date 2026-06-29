import uuid
from datetime import datetime

from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.memory.memory_manager import MemoryManager
from backend.models.memory_record import MemoryRecord


class MemoryAgent(BaseAgent):

    def __init__(self):

        super().__init__("MemoryAgent")

        self.memory = MemoryManager()

    async def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        decision = context.get("decision")

        if decision is None:

            context.complete_agent(self.name)

            return context

        risk = context.get("risk")

        recommendation = context.get(
            "recommendation"
        )

        analytics = context.get(
            "analytics"
        )

        explanation = context.get(
            "explanation"
        )

        parsed_document = context.get(
            "parsed_document"
        )

        query = context.get(
            "query",
            ""
        )

        workflow_id = str(uuid.uuid4())

        metadata = {

            "workflow_id": workflow_id,

            "timestamp": datetime.utcnow().isoformat(),

            "confidence": decision.confidence,

            "document_source":

                getattr(
                    parsed_document,
                    "source",
                    None
                ),

            "document_fingerprint":

                getattr(
                    parsed_document,
                    "fingerprint",
                    None
                )

        }

        value = {

            "query": query,

            "decision":

                decision.model_dump()

                if decision else None,

            "risk":

                risk.model_dump()

                if risk else None,

            "recommendation":

                recommendation.model_dump()

                if recommendation else None,

            "analytics":

                analytics.model_dump()

                if analytics else None,

            "explanation":

                explanation.model_dump()

                if explanation else None

        }

        record = MemoryRecord(

            id=workflow_id,

            agent=self.name,

            key="workflow",

            value=value,

            metadata=metadata

        )

        self.memory.add(record)

        context.set(

            "memory",

            self.memory.all()

        )

        context.complete_agent(
            self.name
        )

        context.add_log(

            "Workflow stored in enterprise memory."

        )

        return context