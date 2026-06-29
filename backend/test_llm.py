import asyncio
from backend.services.llm import LLMService


async def main():
    llm = LLMService()

    response = await llm.generate(
        "Explain in one sentence what an Agentic AI platform is."
    )

    print(response)


if __name__ == "__main__":
    asyncio.run(main())