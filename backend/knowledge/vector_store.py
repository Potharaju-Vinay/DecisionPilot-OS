import chromadb

from chromadb.config import Settings

from backend.models.document_chunk import DocumentChunk

from backend.knowledge.embeddings import EmbeddingService


class EnterpriseVectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma_db",
            settings=Settings(anonymized_telemetry=False)
        )

        self.collection = self.client.get_or_create_collection(
            name="decisionpilot"
        )

        self.embedding_service = EmbeddingService()

    def add_chunks(
        self,
        chunks: list[DocumentChunk]
    ):

        ids = []
        embeddings = []
        documents = []
        metadatas = []

        for chunk in chunks:

            ids.append(chunk.chunk_id)

            documents.append(chunk.content)

            embeddings.append(
                self.embedding_service.generate_embedding(
                    chunk.content
                )
            )

            metadatas.append(chunk.metadata)

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
        self,
        query: str,
        source: str = None,
        top_k: int = 5
    ):

        embedding = self.embedding_service.generate_embedding(
            query
        )

        if source:

            return self.collection.query(

                query_embeddings=[embedding],

                n_results=top_k,

                where={
                    "source": source
                },

                include=[
                    "documents",
                    "metadatas",
                    "distances"
                ]

            )

        return self.collection.query(

            query_embeddings=[embedding],

            n_results=top_k,

            include=[
                "documents",
                "metadatas",
                "distances"
            ]

        )

    def delete_document(
            self,
            document_id: str
    ):
        
        self.collection.delete(
            where={
                "source": document_id
            }
        )