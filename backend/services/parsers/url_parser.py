import requests
from bs4 import BeautifulSoup
from backend.models.parsed_document import ParsedDocument


class URLParser:

    def parse(self, url: str) -> ParsedDocument:

        response = requests.get(url, timeout=15)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator="\n", strip=True)

        return ParsedDocument(
            source=url,
            file_type="url",
            content=text,
            metadata={
                "status_code": response.status_code
            }
        )