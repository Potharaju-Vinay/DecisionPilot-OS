from backend.models.analytics import Analytics

from backend.models.knowledge_package import KnowledgePackage
from backend.models.risk import RiskAssessment
from backend.models.decision_context import DecisionContext
from backend.models.recommendation import Recommendation
from backend.models.explanation import Explanation


class AnalyticsEngine:

    def calculate(

        self,

        knowledge: KnowledgePackage,

        risk: RiskAssessment,

        decision: DecisionContext,

        recommendation: Recommendation,

        explanation: Explanation,

        metrics: dict

    ) -> Analytics:

        total_processing_time = round(

            sum(metrics.values()) * 1000,

            2

        )

        ai_processing_time = round(

            (

                metrics.get("RecommendationAgent", 0)

                +

                metrics.get("ExplainabilityAgent", 0)

            ) * 1000,

            2

        )

        engine_processing_time = round(

            max(

                0,

                total_processing_time - ai_processing_time

            ),

            2

        )

        workflow_efficiency = round(

            (

                engine_processing_time

                /

                max(total_processing_time, 1)

            ) * 100,

            2

        )

        ai_confidence = round(

            (

                knowledge.confidence * 100

                +

                decision.confidence * 100

            ) / 2,

            2

        )

        decision_quality = round(

            (

                decision.business_score * 0.40

                +

                (100 - risk.overall_score) * 0.30

                +

                decision.confidence * 100 * 0.30

            ),

            2

        )

        business_readiness = round(

            (

                decision.business_score * 0.70

                +

                risk.approval_score * 0.30

            ),

            2

        )

        system_reliability = round(

            (

                knowledge.confidence * 100 * 0.40

                +

                (100 - risk.overall_score) * 0.30

                +

                decision.confidence * 100 * 0.30

            ),

            2

        )

        evidence_strength = round(

            knowledge.confidence * 100,

            2

        )

        explainability_score = round(

            min(

                100,

                (

                    len(explanation.evidence) * 5

                    +

                    len(explanation.risks) * 10

                    +

                    len(explanation.recommendations) * 10

                )

            ),

            2

        )

        recommendation_quality = round(

            min(

                100,

                len(recommendation.actions) * 20

            ),

            2

        )

        health_score = round(

            (

                decision_quality

                +

                business_readiness

                +

                system_reliability

            ) / 3,

            2

        )

        if health_score >= 90:

            overall_health = "Excellent"

        elif health_score >= 75:

            overall_health = "Good"

        elif health_score >= 60:

            overall_health = "Average"

        else:

            overall_health = "Needs Attention"

        statistics = risk.statistics

        rule_coverage = statistics.get(

            "coverage",

            0

        )

        triggered_rules = len(

            risk.triggered_rules

        )

        return Analytics(

            business_score=decision.business_score,

            risk_score=risk.overall_score,

            decision_confidence=decision.confidence,

            knowledge_confidence=knowledge.confidence,

            ai_confidence=ai_confidence,

            decision_quality_index=decision_quality,

            business_readiness=business_readiness,

            system_reliability=system_reliability,

            evidence_strength=evidence_strength,

            explainability_score=explainability_score,

            recommendation_quality=recommendation_quality,

            workflow_efficiency=workflow_efficiency,

            rule_coverage=rule_coverage,

            triggered_rules=triggered_rules,

            total_processing_time_ms=total_processing_time,

            engine_processing_time_ms=engine_processing_time,

            ai_processing_time_ms=ai_processing_time,

            overall_health=overall_health,

            workflow_time=round(total_processing_time / 1000, 2),

            documents_processed=1,

            success_rate=100,

            statistics={

                **statistics,

                "health_score": health_score,

                "decision": decision.decision,

                "priority": decision.priority,

                "owner": recommendation.owner,

                "timeline": recommendation.timeline,

                "summary": explanation.summary

            }

        )