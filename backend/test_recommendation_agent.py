import asyncio

from backend.execution.workflow_context import WorkflowContext
from backend.services.input_engine import UniversalInputEngine

from backend.planner.router import PlannerRouter


async def main():

    engine = UniversalInputEngine()

    context = WorkflowContext()

    document = engine.parse(
        "data/samples/demo.txt"
    )

    context.set(
        "parsed_document",
        document
    )

    context.set(
        "query",
        "Should this customer be prioritized?"
    )

    planner = PlannerRouter()

    context = await planner.execute(
        context
    )

    print("\n" + "=" * 60)
    print("DECISION")
    print("=" * 60)
    print(context.get("decision"))

    print("\n" + "=" * 60)
    print("RECOMMENDATION")
    print("=" * 60)
    print(context.get("recommendation"))

    print("\n" + "=" * 60)
    print("MEMORY")
    print("=" * 60)
    print(context.get("memory"))

    print("\n" + "=" * 60)
    print("WORKFLOW LOGS")
    print("=" * 60)
    print(context.logs)

    print("\n" + "=" * 60)
    print("COMPLETED AGENTS")
    print("=" * 60)
    print(context.completed_agents)


if __name__ == "__main__":
    asyncio.run(main())