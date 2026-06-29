from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.models.knowledge_package import KnowledgePackage
from backend.models.graph import KnowledgeGraph

from backend.knowledge.knowledge_graph import KnowledgeGraphBuilder


class GraphAgent(BaseAgent):

    def __init__(self):

        super().__init__("GraphAgent")

        self.builder = KnowledgeGraphBuilder()

    async def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        customer = context.get("customer_discovery")

        risk = context.get("risk")

        decision = context.get("decision")

        recommendation = context.get("recommendation")

        graph = self.builder.build_dashboard_graph(

            customer,

            risk,

            decision,

            recommendation

        )

        context.set(
            "knowledge_graph",
            graph
        )

        context.complete_agent(
            self.name
        )

        context.add_log(

            f"Knowledge graph generated with "

            f"{len(graph.nodes)} nodes and "

            f"{len(graph.edges)} edges."

        )

        return context