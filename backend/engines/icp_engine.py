import re

from backend.models.icp import ICPResult
from backend.models.knowledge_package import KnowledgePackage


class ICPEngine:

    def __init__(self):

        self.rules = {

            "budget": [

                "budget approved",
                "approved budget",
                "allocated budget",
                "funding approved"

            ],

            "authority": [

                "cto",
                "ceo",
                "cio",
                "vp",
                "director",
                "head of"

            ],

            "need": [

                "require",
                "looking for",
                "need",
                "problem",
                "challenge",
                "pain point"

            ],

            "timeline": [

                "this quarter",
                "next quarter",
                "30 days",
                "60 days",
                "90 days",
                "implementation"

            ],

            "industry_fit": [

                "bank",
                "finance",
                "insurance",
                "healthcare",
                "manufacturing",
                "enterprise"

            ],

            "technical_fit": [

                "api",
                "integration",
                "cloud",
                "ai",
                "automation",
                "technical demonstration"

            ]

        }

    def calculate(

        self,

        knowledge: KnowledgePackage

    ) -> ICPResult:

        text = " ".join(

            knowledge.retrieved_chunks

        ).lower()

        buying_signals = []

        missing = []

        score = 0

        def evaluate(name):

            keywords = self.rules[name]

            matched = []

            for keyword in keywords:

                if re.search(

                    re.escape(keyword),

                    text

                ):

                    matched.append(keyword)

            return matched

        budget = evaluate("budget")

        authority = evaluate("authority")

        need = evaluate("need")

        timeline = evaluate("timeline")

        industry = evaluate("industry_fit")

        technical = evaluate("technical_fit")

        if budget:

            score += 20

            buying_signals.extend(budget)

        else:

            missing.append("Budget confirmation")

        if authority:

            score += 20

            buying_signals.extend(authority)

        else:

            missing.append("Decision maker")

        if need:

            score += 20

            buying_signals.extend(need)

        else:

            missing.append("Business need")

        if timeline:

            score += 15

            buying_signals.extend(timeline)

        else:

            missing.append("Timeline")

        if industry:

            score += 15

            buying_signals.extend(industry)

        else:

            missing.append("Industry fit")

        if technical:

            score += 10

            buying_signals.extend(technical)

        else:

            missing.append("Technical readiness")

        return ICPResult(

            score=score,

            qualified=score >= 70,

            budget=bool(budget),

            authority=bool(authority),

            need=bool(need),

            timeline=bool(timeline),

            industry_fit=bool(industry),

            technical_fit=bool(technical),

            buying_signals=buying_signals,

            missing_requirements=missing,

            reasoning=(

                f"ICP qualification completed using evidence "

                f"found in the uploaded document. "

                f"Detected {len(buying_signals)} buying signals "

                f"and {len(missing)} missing qualification criteria."

            )

        )