from backend.planner.workflow import Workflow


class PlannerRouter:

    def __init__(self):

        self.workflow = Workflow()

    async def execute(
        self,
        context
    ):

        return await self.workflow.execute(
            context
        )