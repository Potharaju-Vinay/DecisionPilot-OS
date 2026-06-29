import asyncio

from backend.execution.workflow_context import WorkflowContext
from backend.services.input_engine import UniversalInputEngine
from backend.planner.router import PlannerRouter


async def main():

    engine = UniversalInputEngine()

    context = WorkflowContext()

    context.set(
        "parsed_document",
        engine.parse("data/samples/demo.txt")
    )

    context.set(
        "query",
        "Should this customer be prioritized?"
    )

    planner = PlannerRouter()

    context = await planner.execute(context)

    print()

    print("=" * 60)

    print(context.get("decision"))

    print()

    print("=" * 60)

    print(context.logs)

    print()

    print("=" * 60)

    print(context.completed_agents)


if __name__ == "__main__":
    asyncio.run(main())