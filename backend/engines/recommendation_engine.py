from backend.models.recommendation_context import RecommendationContext
from backend.models.decision_context import DecisionContext
from backend.models.risk import RiskAssessment


class RecommendationEngine:

    def generate(

        self,

        decision: DecisionContext,

        risk: RiskAssessment

    ) -> RecommendationContext:

        if decision.priority == "Critical":

            owner = "VP Sales"

            timeline = "24 Hours"

            urgency = "Immediate"

            impact = "Very High"

            roi = "Very High"

        elif decision.priority == "High":

            owner = "Sales Manager"

            timeline = "2 Days"

            urgency = "High"

            impact = "High"

            roi = "High"

        elif decision.priority == "Medium":

            owner = "Business Analyst"

            timeline = "1 Week"

            urgency = "Normal"

            impact = "Medium"

            roi = "Medium"

        else:

            owner = "CRM System"

            timeline = "Archive"

            urgency = "Low"

            impact = "Low"

            roi = "Low"

        actions = []

        if decision.decision == "Approve":

            actions.extend([

                "Schedule executive meeting",

                "Prepare enterprise proposal",

                "Assign solution architect"

            ])

        elif decision.decision == "Prioritize":

            actions.extend([

                "Schedule technical workshop",

                "Collect additional requirements",

                "Prepare business case"

            ])

        elif decision.decision == "Review":

            actions.extend([

                "Collect missing information",

                "Perform manual review",

                "Recalculate risk"

            ])

        else:

            actions.extend([

                "Reject application",

                "Notify applicant",

                "Archive record"

            ])

        return RecommendationContext(

            priority=decision.priority,

            business_impact=impact,

            urgency=urgency,

            owner=owner,

            timeline=timeline,

            estimated_roi=roi,

            decision_category=decision.decision,

            next_actions=actions,

            statistics={

                "business_score": decision.business_score,

                "risk_score": risk.overall_score,

                "confidence": decision.confidence

            }

        )