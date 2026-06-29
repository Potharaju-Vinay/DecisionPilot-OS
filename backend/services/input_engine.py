from pathlib import Path

from backend.services.parsers.txt_parser import TXTParser
from backend.services.parsers.pdf_parser import PDFParser
from backend.services.parsers.docx_parser import DOCXParser
from backend.services.parsers.csv_parser import CSVParser
from backend.services.parsers.url_parser import URLParser


class UniversalInputEngine:

    def __init__(self):

        self.parsers = {
            ".txt": TXTParser(),
            ".pdf": PDFParser(),
            ".docx": DOCXParser(),
            ".csv": CSVParser(),
        }

        self.url_parser = URLParser()

    def parse(self, source: str):

        if source.startswith("http://") or source.startswith("https://"):
            return self.url_parser.parse(source)

        extension = Path(source).suffix.lower()

        parser = self.parsers.get(extension)

        if parser is None:
            raise ValueError(f"Unsupported file type: {extension}")

        return parser.parse(source)