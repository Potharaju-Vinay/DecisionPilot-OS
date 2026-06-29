from backend.services.input_engine import UniversalInputEngine
from backend.knowledge.chunker import EnterpriseChunker
from backend.knowledge.vector_store import EnterpriseVectorStore


engine = UniversalInputEngine()

document = engine.parse("data/samples/demo.txt")

chunker = EnterpriseChunker()

chunks = chunker.chunk_document(document)

vector_store = EnterpriseVectorStore()

vector_store.add_chunks(chunks)

print("Chunks stored successfully!")

results = vector_store.search(
    "Who requested a technical demonstration?"
)

print(results)