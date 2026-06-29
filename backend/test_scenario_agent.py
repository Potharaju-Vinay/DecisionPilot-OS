import asyncio

from backend.execution.workflow_context import WorkflowContext

from backend.models.parsed_document import ParsedDocument

from backend.agents.knowledge_agent import KnowledgeAgent
from backend.agents.risk_agent import RiskAgent
from backend.agents.decision_agent import DecisionAgent
from backend.agents.scenario_agent import ScenarioAgent


async def main():

    context = WorkflowContext()

    context.set(

        "parsed_document",

        ParsedDocument(

            source="demo.txt",

            file_type="txt",

            content="""
Customer: ABC Technologies

The customer is interested in our AI platform.

Budget approved.

The CTO requested a technical demonstration.

Contract pending.

"""

        )

    )

    context.set(

        "query",

        "Analyze this sales opportunity."

    )

    context = await KnowledgeAgent().execute(
        context
    )

    context = await RiskAgent().execute(
        context
    )

    context = await DecisionAgent().execute(
        context
    )

    context = await ScenarioAgent().execute(
        context
    )

    scenarios = context.get(
        "scenario_result"
    )

    print()

    print("=" * 70)
    print("SCENARIO INTELLIGENCE RESULTS")
    print("=" * 70)

    for scenario in scenarios.scenarios:

        print()

        print("-" * 70)

        print(
            "Scenario :",
            scenario.scenario_name
        )

        print(
            "Description :",
            scenario.description
        )

        print()

        print(
            "Business Score :",
            f"{scenario.original_business_score}"
            " -> "
            f"{scenario.simulated_business_score}"
        )

        print(
            "Risk Score :",
            f"{scenario.original_risk_score}"
            " -> "
            f"{scenario.simulated_risk_score}"
        )

        print(
            "Decision :",
            f"{scenario.original_decision}"
            " -> "
            f"{scenario.simulated_decision}"
        )

        print(
            "Impact :",
            scenario.impact
        )

        print(
            "Confidence :",
            scenario.confidence
        )

        print()

        print(
            "Rule Changes"
        )

        print(
            scenario.changes
        )

    print()

    print("=" * 70)

    print(
        "TOTAL SCENARIOS :",
        scenarios.total_scenarios
    )

    print(
        "STATISTICS"
    )

    print(
        scenarios.statistics
    )

    print("=" * 70)


if __name__ == "__main__":

    asyncio.run(main())