from backend.execution.workflow_context import WorkflowContext
from backend.agents.registry import AgentRegistry


class Planner:

    def __init__(self, registry: AgentRegistry):
        self.registry = registry

    async def execute(self, context: WorkflowContext):

        execution_plan = self.create_execution_plan(context)

        for agent_name in execution_plan:

            agent = self.registry.get(agent_name)

            if agent:
                context.executed_agents.append(agent_name)
                context = await agent.execute(context)

        return context

    def create_execution_plan(self, context: WorkflowContext):

        plan = []

        if context.uploaded_files:
            plan.append("InputAgent")

        plan.append("KnowledgeAgent")
        plan.append("MemoryAgent")
        plan.append("DecisionIntelligenceAgent")
        plan.append("RecommendationAgent")
        plan.append("ExplanationAgent")

        return plan