import re

from backend.models.customer_discovery import CustomerDiscovery
from backend.models.knowledge_package import KnowledgePackage


class CustomerDiscoveryEngine:

    def analyze(
        self,
        knowledge: KnowledgePackage
    ) -> CustomerDiscovery:

        text = "\n".join(
            knowledge.retrieved_chunks
        ).lower()

        discovery = CustomerDiscovery()

        company_patterns = [

            r"Prepared\s+for:\s*(.+)",

            r"([A-Z][A-Za-z&., ]+Pvt\. Ltd\.)",

            r"([A-Z][A-Za-z&., ]+Ltd\.)",

            r"([A-Z][A-Za-z&., ]+Limited)",

            r"([A-Z][A-Za-z&., ]+Technologies)",

            r"([A-Z][A-Za-z&., ]+Solutions)",

            r"([A-Z][A-Za-z&., ]+Corporation)",

            r"([A-Z][A-Za-z&., ]+Inc\.)"

        ]

        text_original = "\n".join(knowledge.retrieved_chunks)

        budget_match = re.search(
            r"Budget\s+Approved:\s*(.+)",
            text_original,
            re.IGNORECASE
        )

        if budget_match:
            discovery.budget = budget_match.group(1).strip()


        timeline_match = re.search(
            r"Timeline:\s*(.+)",
            text_original,
            re.IGNORECASE
        )

        if timeline_match:
            discovery.timeline = timeline_match.group(1).strip()


        industry_match = re.search(
            r"Industry:\s*(.+)",
            text_original,
            re.IGNORECASE
        )

        if industry_match:
            discovery.industry = industry_match.group(1).strip()

        for pattern in company_patterns:

            match = re.search(
                pattern,
                text_original,
                re.IGNORECASE
            )

            if match:

                if match.lastindex:

                    discovery.company = match.group(1).strip()

                else:

                    discovery.company = match.group().strip()

                break

        industry_patterns = {
            
            "Banking": [
                "bank",
                "banking",
                "financial services"
            ],

            "Healthcare": [
                "healthcare",
                "hospital",
                "medical",
                "pharmaceutical"
            ],

            "Insurance": [
                "insurance"
            ],

            "Manufacturing": [
                "manufacturing",
                "factory",
                "industrial"
            ],

            "Technology": [
                "technology",
                "digital transformation",
                "software",
                "cloud",
                "artificial intelligence",
                "ai",
                "enterprise technology"
            ],

            "Retail": [
                "retail",
                "ecommerce",
                "e-commerce"
            ],

            "Telecom": [
                "telecom",
                "telecommunications"
            ]

        }

        for industry, keywords in industry_patterns.items():

            if any(keyword in text for keyword in keywords):

                discovery.industry = industry

                break

        roles = [

            "cto",
            "ceo",
            "cio",
            "vp",
            "director",
            "manager"

        ]

        for role in roles:

            if role in text:

                discovery.decision_makers.append(
                    role.upper()
                )

        pain_keywords = [

            "manual",
            "slow",
            "delay",
            "security",
            "compliance",
            "cost",
            "inefficient"

        ]

        for keyword in pain_keywords:

            if keyword in text:

                discovery.pain_points.append(
                    keyword
                )

        goal_keywords = [

            "automation",
            "growth",
            "efficiency",
            "reduce cost",
            "digital transformation",
            "ai"

        ]

        for keyword in goal_keywords:

            if keyword in text:

                discovery.business_goals.append(
                    keyword
                )

        buying = [

            "budget approved",
            "technical demonstration",
            "pilot",
            "rfp",
            "proposal",
            "contract"

        ]

        for keyword in buying:

            if keyword in text:

                discovery.buying_signals.append(
                    keyword
                )

        objections = [

            "security concern",
            "integration",
            "legal issue",
            "budget limitation",
            "compliance"

        ]

        for keyword in objections:

            if keyword in text:

                discovery.objections.append(
                    keyword
                )

        if discovery.buying_signals:

            discovery.next_best_actions.append(
                "Schedule executive meeting"
            )

        if discovery.objections:

            discovery.next_best_actions.append(
                "Address identified objections"
            )

        discovery.opportunity_score = min(

            100,

            len(discovery.buying_signals) * 15 +

            len(discovery.business_goals) * 10 +

            len(discovery.decision_makers) * 10

        )

        discovery.qualification_summary = (

            f"{len(discovery.buying_signals)} buying signals, "

            f"{len(discovery.decision_makers)} decision makers, "

            f"{len(discovery.pain_points)} pain points identified."

        )

        return discovery