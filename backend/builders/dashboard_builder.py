from backend.execution.workflow_context import WorkflowContext


class DashboardBuilder:

    @staticmethod
    def serialize(obj):

        if obj is None:
            return None

        if hasattr(obj, "model_dump"):
            return obj.model_dump()

        if hasattr(obj, "dict"):
            return obj.dict()

        if isinstance(obj, list):

            return [

                DashboardBuilder.serialize(item)

                for item in obj

            ]

        if isinstance(obj, dict):

            return {

                key: DashboardBuilder.serialize(value)

                for key, value in obj.items()

            }

        return obj

    @staticmethod
    def build(context: WorkflowContext):

        return {

            "customer_discovery":
                DashboardBuilder.serialize(
                    context.get("customer_discovery")
                ),

            "icp":
                DashboardBuilder.serialize(
                    context.get("icp")
                ),

            "risk":
                DashboardBuilder.serialize(
                    context.get("risk")
                ),

            "rule_result":
                DashboardBuilder.serialize(
                    context.get("rule_result")
                ),

            "decision":
                DashboardBuilder.serialize(
                    context.get("decision")
                ),

            "recommendation":
                DashboardBuilder.serialize(
                    context.get("recommendation")
                ),

            "explanation":
                DashboardBuilder.serialize(
                    context.get("explanation")
                ),

            "knowledge_graph":
                DashboardBuilder.serialize(
                    context.get("knowledge_graph")
                ),

            "analytics":
                DashboardBuilder.serialize(
                    context.get("analytics")
                ),

            "personas":
                DashboardBuilder.serialize(
                    context.get("personas")
                ),

            "metrics":
                DashboardBuilder.serialize(
                    context.get("metrics")
                ),

            "completed_agents":
                DashboardBuilder.serialize(
                    context.get("completed_agents")
                ),

            "logs":
                DashboardBuilder.serialize(
                    context.get("logs")
                )

        }