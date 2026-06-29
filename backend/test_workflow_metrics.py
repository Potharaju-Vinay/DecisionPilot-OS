import asyncio

from backend.execution.workflow_context import WorkflowContext
from backend.services.input_engine import UniversalInputEngine
from backend.planner.router import PlannerRouter


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
        "Should this customer be prioritized?"
    )

    planner = PlannerRouter()

    context = await planner.execute(
        context
    )

    print()

    print("=" * 60)

    print("WORKFLOW METRICS")

    print("=" * 60)

    for k, v in context.get_metrics().items():

        print(f"{k:<25}{v} sec")


if __name__ == "__main__":

    asyncio.run(main())