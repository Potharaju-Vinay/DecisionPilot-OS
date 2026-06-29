import time

from backend.execution.workflow_context import WorkflowContext

from backend.agents.registry import (

    AgentRegistry,

    AgentMetadata

)

from backend.agents.knowledge_agent import KnowledgeAgent
from backend.agents.risk_agent import RiskAgent
from backend.agents.decision_agent import DecisionAgent
from backend.agents.memory_agent import MemoryAgent
from backend.agents.recommendation_agent import RecommendationAgent
from backend.agents.explainability_agent import ExplainabilityAgent
from backend.agents.analytics_agent import AnalyticsAgent
from backend.agents.scenario_agent import ScenarioAgent
from backend.agents.learning_agent import LearningAgent
from backend.agents.planner_agent import PlannerAgent
from backend.agents.icp_agent import ICPAgent
from backend.agents.graph_agent import GraphAgent
from backend.agents.customer_discovery_agent import CustomerDiscoveryAgent
from backend.personas.persona_factory import PersonaFactory

class Workflow:

    def __init__(self):

        self.registry = AgentRegistry()

        self.registry.register(
            PlannerAgent(),
            AgentMetadata(
                name="PlannerAgent",
                description="Creates a dynamic execution plan based on the workflow context.",
                capabilities=["planning", "orchestration"],
                inputs=["WorkflowContext"],
                outputs=["ExecutionPlan"],
                tools=[]
            )
        )

        self.registry.register(
            KnowledgeAgent(),
            AgentMetadata(
                name="KnowledgeAgent",
                description="Extracts structured business knowledge from uploaded documents.",
                capabilities=[
                    "knowledge_extraction",
                    "semantic_search",
                    "document_chunking"
                ],
                inputs=["ParsedDocument"],
                outputs=["KnowledgePackage"],
                tools=[
                    "EnterpriseChunker",
                    "EnterpriseVectorStore"
                ]
            )
        )

        self.registry.register(
            
            GraphAgent(),
            AgentMetadata(

                name="GraphAgent",

                description="Builds an enterprise knowledge graph from extracted document entities.",

                capabilities=[

                    "entity_extraction",

                    "relationship_mapping",

                    "knowledge_graph"

                ],

                inputs=[

                    "KnowledgePackage"

                ],

                outputs=[

                    "KnowledgeGraph"

                ],

                tools=[

                    "KnowledgeGraphBuilder"

                ]

            )

        )

        self.registry.register(
            CustomerDiscoveryAgent(),
            AgentMetadata(

                name="CustomerDiscoveryAgent",

                description="Discovers customer profile, buying signals, pain points, business goals and qualification evidence.",

                capabilities=[

                    "customer_discovery",

                    "opportunity_analysis",

                    "buying_signal_detection",

                    "business_goal_identification"
                    
                ],

                inputs=[

                    "KnowledgePackage"

                ],

                outputs=[

                    "CustomerDiscovery"

                ],

                tools=[

                    "CustomerDiscoveryEngine"

                ]

            )

        )

        self.registry.register(
            ICPAgent(),
            AgentMetadata(
                name="ICPAgent",
                description="Qualifies the opportunity against the Ideal Customer Profile.",
                capabilities=[
                    "customer_discovery",
                    "icp_scoring",
                    "qualification"
                ],
                inputs=["KnowledgePackage"],
                outputs=["ICPResult"],
                tools=[
                    "ICPEngine"
                ]
            )
        )

        self.registry.register(
            RiskAgent(),
            AgentMetadata(
                name="RiskAgent",
                description="Performs enterprise risk assessment.",
                capabilities=[
                    "risk_analysis",
                    "rule_evaluation"
                ],
                inputs=["KnowledgePackage"],
                outputs=["RiskAssessment"],
                tools=[
                    "RiskEngine",
                    "RuleEngine"
                ]
            )
        )

        self.registry.register(
            DecisionAgent(),
            AgentMetadata(
                name="DecisionAgent",
                description="Produces business decisions using AI.",
                capabilities=[
                    "decision_intelligence"
                ],
                inputs=[
                    "KnowledgePackage",
                    "RiskAssessment",
                    "ICPResult"
                ],
                outputs=["Decision"],
                tools=[
                    "LLM",
                    "DecisionEngine"
                ]
            )
        )

        self.registry.register(
            MemoryAgent(),
            AgentMetadata(
                name="MemoryAgent",
                description="Stores workflow history for future reasoning.",
                capabilities=[
                    "persistent_memory"
                ],
                inputs=["Decision"],
                outputs=["WorkflowMemory"],
                tools=[
                    "SQLite"
                ]
            )
        )

        self.registry.register(
            RecommendationAgent(),
            AgentMetadata(
                name="RecommendationAgent",
                description="Generates actionable business recommendations.",
                capabilities=[
                    "recommendation_generation"
                ],
                inputs=["Decision"],
                outputs=["Recommendation"],
                tools=[
                    "LLM"
                ]
            )
        )

        self.registry.register(
            ExplainabilityAgent(),
            AgentMetadata(
                name="ExplainabilityAgent",
                description="Explains AI decisions with supporting evidence.",
                capabilities=[
                    "explainability"
                ],
                inputs=["Decision"],
                outputs=["Explanation"],
                tools=[
                    "LLM"
                ]
            )
        )

        self.registry.register(
            AnalyticsAgent(),
            AgentMetadata(
                name="AnalyticsAgent",
                description="Computes enterprise workflow metrics.",
                capabilities=[
                    "analytics",
                    "metrics"
                ],
                inputs=["WorkflowContext"],
                outputs=["Analytics"],
                tools=[
                    "AnalyticsEngine"
                ]
            )
        )

        self.registry.register(
            ScenarioAgent(),
            AgentMetadata(
                name="ScenarioAgent",
                description="Performs what-if analysis.",
                capabilities=[
                    "simulation"
                ],
                inputs=["Decision"],
                outputs=["ScenarioResult"],
                tools=[
                    "ScenarioEngine"
                ]
            )
        )

        self.registry.register(
            LearningAgent(),
            AgentMetadata(
                name="LearningAgent",
                description="Learns from previous workflow executions.",
                capabilities=[
                    "continuous_learning"
                ],
                inputs=["WorkflowHistory"],
                outputs=["LearningInsight"],
                tools=[
                     "LearningEngine"
                ]
            )
        )

        self.persona_factory = PersonaFactory()

    async def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:
        
        workflow_start = time.perf_counter()

        
        planner = self.registry.get(
            "PlannerAgent"
        )

        if planner is None:
            raise ValueError(
                "PlannerAgent not registered."
            )

        start = time.perf_counter()

        context = await planner.execute(
            context
        )

        elapsed = round(

            time.perf_counter() - start,

            3

        )

        context.set_metric(

            planner.name,

            elapsed

        )

        execution_plan = context.get(
            "execution_plan"
        )

        for agent_name in execution_plan:

            agent = self.registry.get(
                agent_name
            )

            if agent is None:

                continue
            print(f"\n========== START {agent.name} ==========")

            start = time.perf_counter()

            context = await agent.execute(
                context
            )

            elapsed = round(

                time.perf_counter() - start,

                3

            )

            print(f"========== END {agent.name} ==========\n")

            context.set_metric(

                agent.name,

                elapsed

            )

        try:
            
            self.build_personas(
                context
            )

        except Exception as e:

            context.add_log(
                f"Persona generation failed: {e}"
            )

        context.add_log(
            "Workflow completed successfully."
        )

        workflow_elapsed = round(

            time.perf_counter() - workflow_start,

            3

        )

        context.set_metric(

            "Workflow",

            workflow_elapsed

        )

            

        return context
    
    def build_personas(
        self,
        context: WorkflowContext
    ):

        start = time.perf_counter()

        context.set(

            "personas",

            self.persona_factory.build_all(
                context
            )

        )

        elapsed = round(

            time.perf_counter() - start,

            3

        )

        context.set_metric(

            "PersonaFactory",

            elapsed

        )

        context.add_log(

            "Personas generated."

        )