import copy
import time

from backend.services.rule_loader import RuleLoader
from backend.services.rule_validator import RuleValidator


class RuleEngine:

    def __init__(self):

        loader = RuleLoader()

        self.rules = loader.load()

        validator = RuleValidator()

        errors = validator.validate(self.rules)

        if errors:

            raise ValueError(
                "\n".join(errors)
            )

    def evaluate(
        self,
        evidence: str
    ):

        start = time.perf_counter()

        text = evidence.lower()

        business_score = 50
        risk_score = 0
        compliance_score = 0
        approval_score = 0

        triggered_rules = []

        audit_trail = []

        for rule in self.rules:

            conditions = rule["condition"]

            if isinstance(conditions, str):

                conditions = [conditions]

            if all(

                keyword.lower() in text

                for keyword in conditions

            ):

                triggered_rules.append(
                    copy.deepcopy(rule)
                )

                audit_trail.append({

                    "rule_id": rule["id"],

                    "rule_name": rule["name"],

                    "category": rule["category"],

                    "score": rule["score"],

                    "matched_text": rule["condition"],

                    "reason": (

                        f"Matched rule "

                        f"'{rule['name']}' "

                        f"because "

                        f"'{rule['condition']}' "

                        f"was found "

                        f"in the uploaded document."

                    )

                })

                if rule["category"] == "business":

                    business_score += rule["score"]

                elif rule["category"] == "risk":

                    risk_score += rule["score"]

                elif rule["category"] == "compliance":

                    compliance_score += rule["score"]

                elif rule["category"] == "approval":

                    approval_score += rule["score"]

        business_score = min(
            business_score,
            100
        )

        elapsed = round(

            (
                time.perf_counter()
                -
                start
            ) * 1000,

            3

        )

        return {

            "business_score": business_score,

            "risk_score": risk_score,

            "compliance_score": compliance_score,

            "approval_score": approval_score,

            "triggered_rules": sorted(

                triggered_rules,

                key=lambda x: x["priority"]

            ),

            "audit_trail": audit_trail,

            "statistics": {

                "total_rules": len(self.rules),

                "matched_rules": len(
                    triggered_rules
                ),

                "coverage": round(

                    len(triggered_rules)
                    /
                    len(self.rules)
                    *
                    100,

                    2

                ),

                "execution_time_ms": elapsed

            }

        }

    def simulate(

        self,

        rule_result: dict,

        disable_rules=None,

        enable_rules=None

    ):

        disable_rules = disable_rules or []

        enable_rules = enable_rules or []

        simulated = copy.deepcopy(
            rule_result
        )

        triggered = []

        for rule in simulated[
            "triggered_rules"
        ]:

            if rule["id"] not in disable_rules:

                triggered.append(rule)

        existing_ids = {

            r["id"]

            for r in triggered

        }

        for rule in self.rules:

            if (

                rule["id"] in enable_rules

                and

                rule["id"] not in existing_ids

            ):

                triggered.append(

                    copy.deepcopy(rule)

                )

        business_score = 50

        risk_score = 0

        compliance_score = 0

        approval_score = 0

        for rule in triggered:

            if rule["category"] == "business":

                business_score += rule["score"]

            elif rule["category"] == "risk":

                risk_score += rule["score"]

            elif rule["category"] == "compliance":

                compliance_score += rule["score"]

            elif rule["category"] == "approval":

                approval_score += rule["score"]

        business_score = min(
            business_score,
            100
        )

        simulated["business_score"] = business_score

        simulated["risk_score"] = risk_score

        simulated["compliance_score"] = compliance_score

        simulated["approval_score"] = approval_score

        simulated["triggered_rules"] = sorted(

            triggered,

            key=lambda x: x["priority"]

        )

        simulated["statistics"]["matched_rules"] = len(
            triggered
        )

        simulated["statistics"]["coverage"] = round(

            len(triggered)

            /

            len(self.rules)

            *

            100,

            2

        )

        return simulated