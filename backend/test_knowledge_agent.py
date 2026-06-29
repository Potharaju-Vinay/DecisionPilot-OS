import asyncio

from backend.execution.workflow_context import WorkflowContext
from backend.services.input_engine import UniversalInputEngine
from backend.agents.knowledge_agent import KnowledgeAgent


async def main():

    context = WorkflowContext()

    engine = UniversalInputEngine()

    document = engine.parse("data/samples/demo.txt")

    context.set("parsed_document", document)

    agent = KnowledgeAgent()

    context = await agent.execute(context)

    print("\n==============================")
    print("Stored Chunks")
    print("==============================")
    print(len(context.get("chunks")))

    package = agent.retrieve(
        "technical demonstration"
    )

    print("\n==============================")
    print("Knowledge Package")
    print("==============================")
    print(package)

    print("\n==============================")
    print("Workflow Logs")
    print("==============================")
    print(context.logs)

    print("\n==============================")
    print("Completed Agents")
    print("==============================")
    print(context.completed_agents)


if __name__ == "__main__":
    asyncio.run(main())