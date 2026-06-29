from backend.engines.rule_engine import RuleEngine

from backend.models.knowledge_package import KnowledgePackage
from backend.models.risk import RiskAssessment


class RiskEngine:

    def __init__(self):

        self.rule_engine = RuleEngine()

        self.base_risk = 50

        self.compliance_weight = 2

    def calculate(
        self,
        knowledge: KnowledgePackage
    ):

        evidence = "\n".join(
            knowledge.retrieved_chunks
        )

        rule_result = self.rule_engine.evaluate(
            evidence
        )

        return self.calculate_from_rule_result(

            knowledge,

            rule_result

        )

    def calculate_from_rule_result(

        self,

        knowledge: KnowledgePackage,

        rule_result: dict

    ):

        business_score = rule_result["business_score"]

        risk_score = rule_result["risk_score"]

        compliance_score = rule_result["compliance_score"]

        approval_score = rule_result["approval_score"]

        overall_score = (

            risk_score

            +

            (
                
                compliance_score
                *
                self.compliance_weight
            )

        )

        if approval_score == 0:

            overall_score += 10

        overall_score = max(

            0,

            min(

                100,

                overall_score

            )

        )

        overall_score = max(

            0,

            min(

                100,

                overall_score

            )

        )

        if overall_score <= 25:

            level = "Low"

        elif overall_score <= 50:

            level = "Medium"

        elif overall_score <= 75:

            level = "High"

        else:

            level = "Critical"

        risk_factors = []

        recommendations = []

        for rule in rule_result["triggered_rules"]:

            risk_factors.append(
                rule["description"]
            )

            if rule["category"] == "risk":

                recommendations.append(
                    f"Mitigate: {rule['name']}"
                )

            elif rule["category"] == "compliance":

                recommendations.append(
                    f"Resolve Compliance: {rule['name']}"
                )

            elif rule["category"] == "business":

                recommendations.append(
                    f"Capitalize on: {rule['name']}"
                )

            elif rule["category"] == "approval":

                recommendations.append(
                    f"Maintain Approval: {rule['name']}"
                )

        summary = (

            f"Business Score: {business_score}, "

            f"Risk Score: {risk_score}, "

            f"Compliance Score: {compliance_score} "

            f"(Weight {self.compliance_weight}x), "

            f"Overall Score: {overall_score}, "

            f"Overall Risk: {level}"

        )

        return {

            "rule_result": rule_result,

            "risk": RiskAssessment(

                overall_risk=level,

                overall_score=overall_score,

                business_score=business_score,

                approval_score=approval_score,

                compliance_score=compliance_score,

                business_risk=max(

                    0,

                    100 - business_score

                ),

                financial_risk=overall_score,

                operational_risk=overall_score,

                technical_risk=overall_score,

                compliance_risk=compliance_score
                *
                self.compliance_weight,

                triggered_rules=rule_result[
                    "triggered_rules"
                ],

                risk_factors=risk_factors,

                recommendations=recommendations,

                statistics=rule_result[
                    "statistics"
                ],

                summary=summary,

                confidence=knowledge.confidence,

                rule_result=rule_result

            )

        }