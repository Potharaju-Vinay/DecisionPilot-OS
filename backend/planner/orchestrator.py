from backend.execution.workflow_context import WorkflowContext
from backend.planner.planner import Planner


class Orchestrator:

    def __init__(self, planner: Planner):
        self.planner = planner

    async def run(self, context: WorkflowContext):

        return await self.planner.execute(context)