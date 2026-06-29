class DocumentExtractor:

    async def extract(self, text: str):

        prompt = f"""
You are an enterprise document extraction engine.

Extract the following information.

Return ONLY valid JSON.

{{
  "company": "",
  "industry": "",
  "budget": "",
  "timeline": "",
  "decision_makers": [],
  "business_goals": [],
  "pain_points": [],
  "buying_signals": []
}}

Document:

{text}
"""