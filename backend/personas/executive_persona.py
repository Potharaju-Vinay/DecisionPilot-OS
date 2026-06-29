from backend.personas.base_persona import BasePersona


class ExecutivePersona(BasePersona):

    def __init__(self):

        super().__init__("Executive")

    def build(self, context):

        customer = context.get("customer_discovery")
        decision = context.get("decision")
        risk = context.get("risk")
        recommendation = context.get("recommendation")

        summary = (
            f"{customer.company} is a strong enterprise opportunity "
            f"with a {decision.decision.lower()} decision."
            if customer and decision
            else "No executive summary available."
        )

        insights = []

        if customer:

            insights.append(
                f"Opportunity Score: {customer.opportunity_score}%"
            )

            insights.append(
                f"Budget: {customer.budget}"
            )

        if risk:

            insights.append(
                f"Overall Risk: {risk.overall_risk}"
            )

        actions = []

        if recommendation:

            if recommendation.actions:

                actions = [

                    action.description

                    for action in recommendation.actions

                ]

            else:

                actions.append(
                    recommendation.summary
                )

        return {

            "summary": summary,

            "insights": insights,

            "actions": actions

        }