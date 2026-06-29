from pathlib import Path
import pandas as pd
from backend.models.parsed_document import ParsedDocument


class CSVParser:

    def parse(self, file_path: str) -> ParsedDocument:

        path = Path(file_path)

        dataframe = pd.read_csv(path)

        return ParsedDocument(
            source=str(path),
            file_type="csv",
            content=dataframe.to_string(index=False),
            metadata={
                "file_name": path.name,
                "file_size": path.stat().st_size,
                "rows": len(dataframe),
                "columns": len(dataframe.columns)
            }
        )