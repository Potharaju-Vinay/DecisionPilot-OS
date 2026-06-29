from backend.knowledge.embeddings import EmbeddingService

service = EmbeddingService()

embedding = service.generate_embedding(
    "DecisionPilot is an enterprise Agentic AI platform."
)

print(f"Embedding Length: {len(embedding)}")
print(embedding[:10])