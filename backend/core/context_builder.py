from backend.models.decision_context import DecisionContext


class ContextBuilder:

    def build(

        self,

        context

    ):

        knowledge = context.get(
            "knowledge"
        )

        risk = context.get(
            "risk"
        )

        rules = context.get(
            "business_rules"
        )

        return DecisionContext(

            query=context.get("query"),

            knowledge=knowledge.retrieved_chunks,

            business_score=rules["score"],

            business_reasons=rules["reasons"],

            risk_score=risk.overall_score,

            risk_level=risk.overall_risk

        )