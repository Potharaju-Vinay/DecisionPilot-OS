class RuleValidator:

    REQUIRED_FIELDS = [

        "id",

        "category",

        "name",

        "condition",

        "score",

        "priority"

    ]

    def validate(self, rules):

        ids = set()

        errors = []

        for rule in rules:

            for field in self.REQUIRED_FIELDS:

                if field not in rule:

                    errors.append(

                        f"{rule.get('id')} missing {field}"

                    )

            if rule["id"] in ids:

                errors.append(

                    f"Duplicate ID {rule['id']}"

                )

            ids.add(

                rule["id"]

            )

        return errors