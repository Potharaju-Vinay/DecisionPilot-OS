import json
from pathlib import Path


class RuleLoader:

    def __init__(self):

        self.rule_file = (
            Path(__file__).parent.parent
            / "rules"
            / "rules.json"
        )

    def load(self):

        with open(

            self.rule_file,

            "r",

            encoding="utf-8"

        ) as f:

            data = json.load(f)

        return data["rules"]