from pathlib import Path
from pypdf import PdfReader
from backend.models.parsed_document import ParsedDocument


class PDFParser:

    def parse(self, file_path: str) -> ParsedDocument:

        path = Path(file_path)

        reader = PdfReader(path)

        content = ""

        for page in reader.pages:
            text = page.extract_text()
            if text:
                content += text + "\n"

        return ParsedDocument(
            source=str(path),
            file_type="pdf",
            content=content,
            metadata={
                "file_name": path.name,
                "file_size": path.stat().st_size,
                "pages": len(reader.pages)
            }
        )