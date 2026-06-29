from abc import ABC, abstractmethod
from backend.execution.workflow_context import WorkflowContext


class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    async def execute(self, context: WorkflowContext) -> WorkflowContext:
        """
        Every agent must implement this method.
        """
        pass