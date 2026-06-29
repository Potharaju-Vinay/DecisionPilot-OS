import asyncio

from backend.execution.workflow_context import WorkflowContext

from backend.services.input_engine import UniversalInputEngine

from backend.agents.knowledge_agent import KnowledgeAgent
from backend.agents.decision_agent import DecisionAgent


async def main():

    context = WorkflowContext()

    engine = UniversalInputEngine()

    document = engine.parse(
        "data/samples/demo.txt"
    )

    context.set(
        "parsed_document",
        document
    )

    context.set(
        "query",
        "Should the customer be prioritized?"
    )

    knowledge = KnowledgeAgent()

    context = await knowledge.execute(
        context
    )

    decision = DecisionAgent()

    context = await decision.execute(
        context
    )

    print()

    print("=" * 60)

    print(context.get("decision"))

    print("=" * 60)

    print()

    print(context.logs)


asyncio.run(main())