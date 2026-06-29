from collections import Counter

from backend.models.learning import LearningInsight
from backend.models.risk import RiskAssessment
from backend.models.decision_context import DecisionContext


class LearningEngine:

    def generate(

        self,

        decision: DecisionContext,

        risk: RiskAssessment

    ) -> LearningInsight:

        total_decisions = 1

        approval_rate = 0.0

        manual_review_rate = 0.0

        rejection_rate = 0.0

        if decision.decision == "Approve":

            approval_rate = 100.0

        elif decision.decision == "Manual Review":

            manual_review_rate = 100.0

        elif decision.decision == "Reject":

            rejection_rate = 100.0

        triggered_rules = [

            rule["name"]

            for rule in risk.triggered_rules

        ]

        if triggered_rules:

            most_triggered_rule = Counter(

                triggered_rules

            ).most_common(1)[0][0]

        else:

            most_triggered_rule = "None"

        if risk.overall_score >= 50:

            recommendation = (

                "Reduce enterprise risk before approval."

            )

        elif risk.compliance_score >= 20:

            recommendation = (

                "Prioritize compliance verification."

            )

        elif decision.decision == "Manual Review":

            recommendation = (

                "Escalate for expert review."

            )

        else:

            recommendation = (

                "Current decision policy is performing well."

            )

        summary = (

            f"{decision.decision} decision generated "

            f"with Business Score "

            f"{decision.business_score} "

            f"and Overall Risk "

            f"{risk.overall_score}."

        )

        return LearningInsight(

            total_decisions=total_decisions,

            approval_rate=approval_rate,

            manual_review_rate=manual_review_rate,

            rejection_rate=rejection_rate,

            average_business_score=decision.business_score,

            average_risk_score=risk.overall_score,

            most_triggered_rule=most_triggered_rule,

            learning_summary=summary,

            improvement_recommendation=recommendation,

            statistics={

                "triggered_rules": len(

                    risk.triggered_rules

                ),

                "knowledge_confidence": risk.confidence,

                "decision": decision.decision

            }

        )