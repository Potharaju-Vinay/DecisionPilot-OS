from backend.models.knowledge_package import KnowledgePackage
from backend.models.risk import RiskAssessment
from backend.models.decision_context import DecisionContext


class DecisionEngine:

    def __init__(self):

        self.strategy = "Balanced"

    def evaluate(
        self,
        knowledge: KnowledgePackage,
        risk: RiskAssessment,
        rule_result: dict
    ) -> DecisionContext:

        business_score = rule_result.get(
            "business_score",
            50
        )

        approval_score = rule_result.get(
            "approval_score",
            0
        )

        compliance_score = rule_result.get(
            "compliance_score",
            0
        )

        overall_risk = risk.overall_score

        confidence = round(

            (
                knowledge.confidence * 0.30 +

                (business_score / 100) * 0.40 +

                ((100 - overall_risk) / 100) * 0.30

            ),

            2

        )

        if compliance_score >= 20:

            decision = "Manual Review"

            priority = "Critical"

            approval = "Compliance Team"

        elif overall_risk >= 40:

            decision = "Manual Review"

            priority = "High"

            approval = "Risk Team"

        elif business_score >= 90 and overall_risk <= 20:

            decision = "Approve"

            priority = "Critical"

            approval = "Executive"

        elif business_score >= 75:

            decision = "Prioritize"

            priority = "High"

            approval = "Manager"

        elif business_score >= 50:

            decision = "Review"

            priority = "Medium"

            approval = "Analyst"

        else:

            decision = "Reject"

            priority = "Low"

            approval = "Automatic"

        reasoning = [

            f"Business Score : {business_score}",

            f"Overall Risk : {overall_risk}",

            f"Compliance Score : {compliance_score}",

            f"Approval Score : {approval_score}",

            f"Knowledge Confidence : {knowledge.confidence}",

            f"Triggered Rules : {len(rule_result.get('triggered_rules', []))}",

            f"Strategy : {self.strategy}"

        ]

        return DecisionContext(

            decision=decision,

            priority=priority,

            confidence=confidence,

            business_score=business_score,

            risk_score=overall_risk,

            approval_level=approval,

            strategy=self.strategy,

            triggered_rules=rule_result.get(
                "triggered_rules",
                []
            ),

            reasoning=reasoning,

            statistics=rule_result.get(
                "statistics",
                {}
            )

        )