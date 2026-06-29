import asyncio

from backend.services.llm import LLMService


async def main():

    llm = LLMService()

    print("Sending request to Gemini...")

    response = await llm.generate(
        "Reply with exactly: Hello DecisionPilot"
    )

    print("\nResponse:")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())