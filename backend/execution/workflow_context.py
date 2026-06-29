from typing import Any


class WorkflowContext:

    def __init__(self):

        self.data = {}

        self.logs = []

        self.completed_agents = []

        self.metrics = {}

    def set(
        self,
        key: str,
        value: Any
    ):

        self.data[key] = value

    def get(
        self,
        key: str,
        default=None
    ):

        return self.data.get(
            key,
            default
        )

    def add_log(
        self,
        message: str
    ):

        self.logs.append(message)

        self.data["logs"] = self.logs

    def complete_agent(
        self,
        agent_name: str
    ):

        self.completed_agents.append(agent_name)

        self.data["completed_agents"] = self.completed_agents

    def set_metric(
        self,
        key: str,
        value
    ):

        self.metrics[key] = value

        self.data["metrics"] = self.metrics

    def get_metric(
        self,
        key: str
    ):

        return self.metrics.get(key)

    def get_metrics(self):

        return self.metrics