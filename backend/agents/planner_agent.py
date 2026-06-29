from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext


class PlannerAgent(BaseAgent):

    def __init__(self):

        super().__init__("PlannerAgent")

    async def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        query = context.get(
            "query",
            ""
        ).lower()

        planning_context = {

            "query": query,

            "has_document":

                context.get(
                    "parsed_document"
                ) is not None,

            "has_memory":

                context.get(
                    "memory"
                ) is not None,

            "has_rules":

                context.get(
                    "rule_result"
                ) is not None,

            "scenario_mode":

                any(

                    word in query

                    for word in [

                        "scenario",

                        "what if",

                        "simulation"

                    ]

                ),

            "analytics_mode":

                any(

                    word in query

                    for word in [

                        "analytics",

                        "dashboard",

                        "report"

                    ]

                ),

            "decision_mode":

                any(

                    word in query

                    for word in [

                        "approve",

                        "decision",

                        "proposal",

                        "qualification",

                        "analyze"

                    ]

                )

        }

        execution_plan = []
        
        if planning_context["has_document"]:
            
            execution_plan.extend([

                "KnowledgeAgent",

                "CustomerDiscoveryAgent",

                "ICPAgent",

                "RiskAgent",

                "DecisionAgent",

                "RecommendationAgent",

                "ExplainabilityAgent",

                "GraphAgent",

                "AnalyticsAgent",

                "MemoryAgent"

            ])


        if planning_context["scenario_mode"]:
            
            execution_plan.append(
                "ScenarioAgent"
            )


        if planning_context["analytics_mode"]:
            
            execution_plan.append(

                "LearningAgent"

            )

        

        execution_plan = list(
            dict.fromkeys(
                execution_plan
            )
        )

        context.set(

            "planning_context",

            planning_context

        )

        context.set(

            "execution_plan",

            execution_plan

        )

        context.complete_agent(
            self.name
        )

        context.add_log(
            f"Planner created execution plan: {execution_plan}"
        )

        return context