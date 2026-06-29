from backend.agents.base_agent import BaseAgent
from backend.execution.workflow_context import WorkflowContext

from backend.knowledge.chunker import EnterpriseChunker
from backend.knowledge.vector_store import EnterpriseVectorStore

from backend.models.knowledge_package import KnowledgePackage

from backend.planner.register_tools import tool_registry


class KnowledgeAgent(BaseAgent):

    def __init__(self):

        super().__init__("KnowledgeAgent")


        self.chunker = tool_registry.get(
            "chunker"
        )

        self.vector_store = tool_registry.get(
            "vector_store"
        )

    async def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        parsed_document = context.get(
            
            "parsed_document"
        )

        if parsed_document is None:

            context.add_log(

                "KnowledgeAgent skipped: No document available."

            )

            context.complete_agent(
                self.name
            )

            return context

        self.vector_store.delete_document(
            parsed_document.source
        )

        chunks = self.chunker.chunk_document(
            parsed_document
        )

        self.vector_store.add_chunks(
            chunks
        )

        context.set(
            "chunks",
            chunks
        )

        query = context.get(
            "query",
            "document summary"
        )

        package = self.retrieve(

            query,

            parsed_document.source

        )

        print("\n========== RETRIEVED CHUNKS ==========\n")

        for i, chunk in enumerate(package.retrieved_chunks):

            print(f"\n------ Chunk {i+1} ------\n")

            print(chunk)

        print("\n======================================\n")

        context.set(
            "knowledge",
            package
        )

        context.complete_agent(
            self.name
        )

        context.add_log(
            f"{len(chunks)} chunks stored in ChromaDB."
        )

        return context

    def retrieve(
        self,
        query: str,
        source: str,
        top_k: int = 5
    ) -> KnowledgePackage:

        results = self.vector_store.search(
            query=query,
            source=source,
            top_k=top_k
        )

        documents = results.get(
            "documents",
            [[]]
        )[0]

        metadatas = results.get(
            "metadatas",
            [[]]
        )[0]

        distances = results.get(
            "distances",
            [[]]
        )[0]

        sources = [
            metadata.get(
                "source",
                ""
            )
            for metadata in metadatas
        ]

        if distances:

            avg_distance = sum(
                distances
            ) / len(distances)

            confidence = round(
                1 / (1 + avg_distance),
                2
            )

        else:

            avg_distance = None

            confidence = 0.0

        return KnowledgePackage(

            query=query,

            retrieved_chunks=documents,

            sources=sources,

            confidence=confidence,

            metadata={

                "results": len(documents),

                "top_k": top_k,

                "avg_distance": round(
                    avg_distance,
                    4
                ) if avg_distance is not None else None,

                "retrieved_sources": len(
                    set(sources)
                )

            }

        )