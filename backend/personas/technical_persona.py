from backend.personas.base_persona import BasePersona


class TechnicalPersona(BasePersona):

    def __init__(self):

        super().__init__("Technical")

    def build(self, context):

        graph = context.get("knowledge_graph")
        knowledge = context.get("knowledge")
        recommendation = context.get("recommendation")

        summary = (
            "Technical deployment is feasible."
            if graph
            else "No technical summary available."
        )

        insights = []

        if graph:

            insights.append(
                f"Knowledge Graph Nodes: {len(graph.nodes)}"
            )

            insights.append(
                f"Knowledge Graph Edges: {len(graph.edges)}"
            )

        if knowledge:

            insights.append(
                f"Knowledge Sources: {len(knowledge.sources)}"
            )

        actions = []

        if recommendation:

            if recommendation.actions:

                actions = [

                    action.description

                    for action in recommendation.actions[:3]

                ] 

        return {

            "summary": summary,

            "insights": insights,

            "actions": actions

        }