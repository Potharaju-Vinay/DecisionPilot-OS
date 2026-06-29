from backend.engines.rule_engine import RuleEngine


engine = RuleEngine()

text = """
Customer budget approved.

The CTO requested a technical demonstration.
"""

result = engine.evaluate(text)

print(result)