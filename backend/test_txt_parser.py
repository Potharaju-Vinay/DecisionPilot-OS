from backend.services.parsers.txt_parser import TXTParser

parser = TXTParser()

result = parser.parse("data/samples/demo.txt")

print(result)