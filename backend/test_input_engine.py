from backend.services.input_engine import UniversalInputEngine

engine = UniversalInputEngine()

result = engine.parse("data/samples/demo.txt")

print(result)