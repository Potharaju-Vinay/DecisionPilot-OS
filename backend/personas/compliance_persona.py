from backend.personas.base_persona import BasePersona


class CompliancePersona(BasePersona):

    def __init__(self):

        super().__init__("Compliance")

    def build(self, context):

        risk = context.get("risk")
        recommendation = context.get("recommendation")

        summary = (
            f"Current compliance status is {risk.overall_risk} risk."
            if risk
            else "No compliance summary available."
        )

        insights = []

        if risk:

            insights.append(
                f"Compliance Score: {risk.compliance_score}"
            )

            insights.append(
                f"Overall Risk: {risk.overall_risk}"
            )

        actions = []

        if recommendation:

            if recommendation.actions:

                actions = [

                    action.description

                    for action in recommendation.actions[:3]

                ] 

        return {

            "summary": summary,

            "insights": insights,

            "actions": actions

        }