from backend.services.parsers.pdf_parser import PDFParser

parser = PDFParser()

result = parser.parse("data/samples/sample.pdf")

print(result)