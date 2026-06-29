from backend.models.explanation_context import ExplanationContext

from backend.models.decision_context import DecisionContext
from backend.models.risk import RiskAssessment
from backend.models.knowledge_package import KnowledgePackage


class ExplainabilityEngine:

    def generate(

        self,

        knowledge: KnowledgePackage,

        decision: DecisionContext,

        risk: RiskAssessment

    ) -> ExplanationContext:

        if decision.confidence >= 0.9:

            evidence_strength = "Very Strong"

        elif decision.confidence >= 0.75:

            evidence_strength = "Strong"

        elif decision.confidence >= 0.5:

            evidence_strength = "Moderate"

        else:

            evidence_strength = "Weak"

        path = [

            "Knowledge Retrieved",

            "Business Rules Evaluated",

            "Risk Calculated",

            "Decision Generated"

        ]

        factors = []

        if decision.business_score >= 90:

            factors.append(
                "Excellent business opportunity"
            )

        if risk.overall_risk == "Low":

            factors.append(
                "Minimal business risk"
            )

        if decision.confidence >= 0.8:

            factors.append(
                "High AI confidence"
            )

        if len(
            risk.triggered_rules
        ) > 0:

            factors.append(
                f"{len(risk.triggered_rules)} business rules matched"
            )

        return ExplanationContext(

            decision=decision.decision,

            confidence=decision.confidence,

            business_score=decision.business_score,

            risk_score=risk.overall_score,

            approval_level=decision.approval_level,

            evidence_strength=evidence_strength,

            decision_path=path,

            evidence=knowledge.retrieved_chunks,

            triggered_rules=risk.triggered_rules,

            key_factors=factors,

            statistics={

                "knowledge_confidence":
                    knowledge.confidence,

                "matched_rules":
                    len(risk.triggered_rules)

            }

        )