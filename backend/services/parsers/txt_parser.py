from pathlib import Path
from backend.models.parsed_document import ParsedDocument


class TXTParser:

    def parse(self, file_path: str) -> dict:
        path = Path(file_path)

        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        return ParsedDocument(
            source=str(path),
            file_type="txt",
            content=content,
            metadata={
                "file_name": path.name,
                "file_size": path.stat().st_size
            }
        )