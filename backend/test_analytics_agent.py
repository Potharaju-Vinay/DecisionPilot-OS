import asyncio

from backend.execution.workflow_context import WorkflowContext
from backend.models.parsed_document import ParsedDocument

from backend.planner.router import PlannerRouter


async def main():

    with open(
        "data/samples/demo.txt",
        "r",
        encoding="utf-8"
    ) as f:

        text = f.read()

    parsed_document = ParsedDocument(
        
        source="data/samples/demo.txt",

        file_type="txt",

        content=text,

        title="Demo Customer",

        metadata={}

    )

    context = WorkflowContext()

    context.set(
        "parsed_document",
        parsed_document
    )

    context.set(
        "query",
        "technical demonstration"
    )

    planner = PlannerRouter()

    context = await planner.execute(
        context
    )

    print("\n" + "=" * 60)
    print("ANALYTICS")
    print("=" * 60)

    print(
        context.get(
            "analytics"
        )
    )

    print("\n" + "=" * 60)
    print("WORKFLOW METRICS")
    print("=" * 60)

    print(
        context.metrics
    )

    print("\n" + "=" * 60)
    print("WORKFLOW LOGS")
    print("=" * 60)

    print(
        context.logs
    )


if __name__ == "__main__":

    asyncio.run(
        main()
    )