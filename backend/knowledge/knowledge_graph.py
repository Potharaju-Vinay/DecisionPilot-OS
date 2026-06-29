import re

from backend.models.graph import (
    KnowledgeGraph,
    GraphNode,
    GraphEdge
)


class KnowledgeGraphBuilder:

    def build(
        self,
        text: str
    ) -> KnowledgeGraph:

        nodes = []

        edges = []

        entities = {

            "Company": [

                r"Prepared\s+for:\s*(.+)",

                r"\b[A-Z][A-Za-z&., ]+Pvt\. Ltd\.\b",

                r"\b[A-Z][A-Za-z&., ]+Ltd\.\b",

                r"\b[A-Z][A-Za-z&., ]+Limited\b",

                r"\b[A-Z][A-Za-z&., ]+Inc\b",

                r"\b[A-Z][A-Za-z&., ]+Corporation\b"

            ],

            "Person": [

                r"\bCTO\b",

                r"\bCEO\b",

                r"\bCIO\b"

            ],

            "Business": [

                r"technical demonstration",

                r"proposal",

                r"contract",

                r"compliance",

                r"automation",

                r"knowledge graph",

                r"artificial intelligence",

                r"AI"

            ],

        }

        company = None

        node_id = 1

        for entity_type, patterns in entities.items():

            for pattern in patterns:

                matches = re.findall(
                    pattern,
                    text,
                    flags=re.IGNORECASE
                )

                for match in matches:

                    value = match.strip()

                    nodes.append(

                        GraphNode(

                            id=f"N{node_id}",

                            type=entity_type,

                            value=value

                        )

                    )

                    if entity_type == "Company":

                        company = f"N{node_id}"

                    elif company:

                        if entity_type == "Industry":

                            relation = "operates_in"

                        elif entity_type == "Person":

                            relation = "managed_by"

                        elif entity_type == "Budget":

                            relation = "approved_budget"

                        elif entity_type == "Timeline":

                            relation = "scheduled_for"

                        elif entity_type == "Business":

                            relation = "supports"

                        else:

                            relation = "related_to"

                        edges.append(

                            GraphEdge(

                                source=company,

                                target=f"N{node_id}",

                                relation=relation

                            )

                        )

                    node_id += 1

        return KnowledgeGraph(

            nodes=nodes,

            edges=edges

        )
    
    def build_dashboard_graph(
        self,
        customer,
        risk,
        decision,
        recommendation
    ):

        nodes = []

        edges = []

        print("\n========== GRAPH DEBUG ==========")
        print("Goals:", customer.business_goals)
        print("Signals:", customer.buying_signals)
        print("=================================\n")

        nodes.append(

            GraphNode(

                id="1",

                type="Company",

                value=customer.company or "Unknown Company"

            )

        )

        nodes.append(

            GraphNode(

                id="2",

                type="Industry",

                value=customer.industry or "Unknown Industry"

            )
 
        )

        nodes.append(

            GraphNode(

                id="3",

                type="Person",

                value=customer.decision_makers[0]

                if customer.decision_makers

                else "Unknown"

            )

        )

        nodes.append(

            GraphNode(

                id="4",

                type="Budget",

                value=customer.budget or "Not Available"

            )

        )

        nodes.append(

            GraphNode(

                id="5",

                type="Timeline",

                value=customer.timeline or "Not Available"

            )

        )

        goal_nodes = []

        next_id = 6

        for goal in customer.business_goals:

            nodes.append(

                GraphNode(

                    id=str(next_id),

                    type="Goal",

                    value=goal

                )

            )

            goal_nodes.append(str(next_id))

            next_id += 1


        signal_nodes = []

        signal_id = next_id

        for signal in customer.buying_signals:

            nodes.append(

                GraphNode(

                    id=str(signal_id),

                    type="Signal",

                    value=signal

                )

            )

            signal_nodes.append(str(signal_id))

            signal_id += 1


        risk_id = str(signal_id)

        nodes.append(

            GraphNode(

                id=risk_id,

                type="Risk",

                value=risk.overall_risk

            )

        )

        signal_id += 1

        decision_id = str(signal_id)

        nodes.append(

            GraphNode(

                id=decision_id,

                type="Decision",

                value=decision.decision

            )

        ) 

        signal_id += 1

        action_id = str(signal_id)

        action = "Pilot Implementation"

        nodes.append(

            GraphNode(

                id=action_id,

                type="Action",

                value=action

            )

        )

        signal_id += 1


        score_id = str(signal_id)

        nodes.append(

            GraphNode(

                id=score_id,

                type="Signal",

                value=f"Opportunity Score: {customer.opportunity_score}%"

            )

        )

        signal_id += 1


        # Company -> Industry

        edges.append(

            GraphEdge(

                source="1",

                target="2",

                relation="Industry"

            )

        )

        # Company -> Decision Maker

        edges.append(

            GraphEdge(

                source="1",

                target="3",

                relation="Decision Maker"

            )

        )

        # Company -> Budget

        edges.append(

            GraphEdge(

                source="1",

                target="4",

                relation="Budget"

            )

        )

        # Company -> Timeline

        edges.append(

            GraphEdge(

                source="1",

                target="5",

                relation="Timeline"

            )

        )

        previous = "1"

        # Connect Company -> Goals
        for goal in goal_nodes:

            edges.append(

                GraphEdge(

                    source=previous,

                    target=goal,

                    relation="Business Goal"

                )

            )

            

        

        # Connect Goals -> Buying Signals
        for signal in signal_nodes:

            edges.append(

                GraphEdge(

                    source=previous,

                    target=signal,

                    relation="Buying Signal"

                )

            )

            

        # Connect Last Signal -> Risk
        edges.append(

            GraphEdge(

                source=previous,

                target=risk_id,

                relation="Risk"

            )

        )

        previous = risk_id

        # Risk -> Decision
        edges.append(

            GraphEdge(

                source=risk_id,

                target=decision_id,

                relation="AI Decision"

            )

        )

        previous = decision_id

        # Decision -> Recommendation
        edges.append(

            GraphEdge(
 
                source=decision_id,

                target=action_id,

                relation="Recommendation"

            )

        )
        previous = action_id

        # Recommendation -> Opportunity Score
        edges.append(

            GraphEdge(

                source=action_id,

                target=score_id,

                relation="Opportunity Score"

            )

        )

        print("\n===== GRAPH NODES =====")

        for node in nodes:

            print(node.id, node.type, node.value)

        print("Total Nodes:", len(nodes))

        print("\n===== GRAPH EDGES =====")

        for edge in edges:

            print(edge.source, "->", edge.target)

        print("Total Edges:", len(edges))

        
        return KnowledgeGraph(

            nodes=nodes,

            edges=edges

        )