from backend.services.input_engine import UniversalInputEngine
from backend.knowledge.chunker import EnterpriseChunker


engine = UniversalInputEngine()

document = engine.parse("data/samples/demo.txt")

chunker = EnterpriseChunker()

chunks = chunker.chunk_document(document)

print(f"Total Chunks: {len(chunks)}")

for chunk in chunks:
    print("=" * 60)
    print(chunk)