from backend.personas.base_persona import BasePersona


class SalesPersona(BasePersona):

    def __init__(self):

        super().__init__("Sales")

    def build(self, context):

        customer = context.get("customer_discovery")
        decision = context.get("decision")
        recommendation = context.get("recommendation")
        icp = context.get("icp")

        summary = (
            f"{customer.company} is sales-ready with a high conversion opportunity."
            if customer
            else "No sales summary available."
        )

        insights = []

        if icp:
            insights.append(f"ICP Score: {icp.score}")

        if customer:
            insights.append(f"Opportunity Score: {customer.opportunity_score}%")

            insights.extend(customer.buying_signals[:2])

        actions = []

        if recommendation:

            if recommendation.actions:

                actions = [

                    action.description

                    for action in recommendation.actions

                ]

            else:

                actions.append(recommendation.summary)

        return {

            "summary": summary,

            "insights": insights,

            "actions": actions

        }