from backend.engines.rule_engine import RuleEngine
from backend.engines.risk_engine import RiskEngine
from backend.engines.decision_engine import DecisionEngine

from backend.models.knowledge_package import KnowledgePackage
from backend.models.scenario import Scenario
from backend.models.scenario import ScenarioResult


class ScenarioEngine:

    def __init__(self):

        self.rule_engine = RuleEngine()

        self.risk_engine = RiskEngine()

        self.decision_engine = DecisionEngine()

    def generate(

        self,

        knowledge: KnowledgePackage,

        current_rule_result: dict,

        current_decision: str

    ) -> ScenarioResult:

        templates = [

            {

                "name": "Budget Removed",

                "description": "Budget approval removed.",

                "disable_rules": [

                    "BR001",

                    "AP001"

                ],

                "enable_rules": []

            },

            {

                "name": "Executive Sponsor Removed",

                "description": "CTO no longer involved.",

                "disable_rules": [

                    "BR002"

                ],

                "enable_rules": []

            },

            {

                "name": "Legal Issue Added",

                "description": "Legal issue detected.",

                "disable_rules": [],

                "enable_rules": [

                    "RS001"

                ]

            },

            {

                "name": "Compliance Review",

                "description": "Compliance review required.",

                "disable_rules": [],

                "enable_rules": [

                    "CP001"

                ]

            },

            {

                "name": "Contract Pending",

                "description": "Contract still pending.",

                "disable_rules": [],

                "enable_rules": [

                    "RS002"

                ]

            }

        ]

        scenarios = []

        current_result = self.risk_engine.calculate_from_rule_result(

            knowledge,

            current_rule_result

        )

        current_risk = current_result["risk"]

        for template in templates:

            simulated_rules = self.rule_engine.simulate(

                current_rule_result,

                disable_rules=template["disable_rules"],

                enable_rules=template["enable_rules"]

            )

            risk_result = self.risk_engine.calculate_from_rule_result(

                knowledge,

                simulated_rules

            )

            simulated_risk = risk_result["risk"]

            simulated_decision = self.decision_engine.evaluate(

                knowledge,

                simulated_risk,

                simulated_rules

            )

            impact = self._calculate_impact(

                current_rule_result["business_score"],

                simulated_rules["business_score"],

                current_risk.overall_score,

                simulated_risk.overall_score,

                current_decision,

                simulated_decision.decision

            )

            scenarios.append(

                Scenario(

                    scenario_name=template["name"],

                    description=template["description"],

                    changes={

                        "disabled_rules": template["disable_rules"],

                        "enabled_rules": template["enable_rules"]

                    },

                    original_business_score=current_rule_result["business_score"],

                    simulated_business_score=simulated_rules["business_score"],

                    original_risk_score=current_risk.overall_score,

                    simulated_risk_score=simulated_risk.overall_score,

                    original_decision=current_decision,

                    simulated_decision=simulated_decision.decision,

                    impact=impact,

                    confidence=simulated_decision.confidence

                )

            )

        return ScenarioResult(

            scenarios=scenarios,

            total_scenarios=len(scenarios),

            statistics={

                "generated": len(scenarios),

                "engine": "Scenario Intelligence Engine"

            }

        )

    def _calculate_impact(

        self,

        original_business,

        new_business,

        original_risk,

        new_risk,

        original_decision,

        new_decision

    ):

        if original_decision != new_decision:

            if new_decision in [

                "Reject",

                "Manual Review"

            ]:

                return "Critical"

            elif new_decision == "Review":

                return "High"

            elif new_decision == "Prioritize":

                return "Medium"

        business_change = abs(

            original_business

            -

            new_business

        )

        risk_change = abs(

            original_risk

            -

            new_risk

        )

        score = business_change + risk_change

        if score >= 40:

            return "Critical"

        elif score >= 25:

            return "High"

        elif score >= 10:

            return "Medium"

        return "Low"