import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.models.document_chunk import DocumentChunk
from backend.models.parsed_document import ParsedDocument


class EnterpriseChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def chunk_document(
        self,
        document: ParsedDocument
    ):

        texts = self.splitter.split_text(document.content)

        chunks = []

        for index, text in enumerate(texts):

            chunk = DocumentChunk(

                chunk_id=str(uuid.uuid4()),

                document_id=document.source,

                chunk_index=index,

                content=text,

                metadata={
                    "source": document.source,
                    "file_type": document.file_type,
                    "chunk_index": index,
                    **document.metadata
                }
            )

            chunks.append(chunk)

        return chunks