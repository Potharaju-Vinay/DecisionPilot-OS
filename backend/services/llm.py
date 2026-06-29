from langchain_google_genai import ChatGoogleGenerativeAI

from backend.core.provider import LLMProvider
from backend.core.llm_manager import LLMManager
from backend.core.config import (
    GOOGLE_API_KEY,
    LLM_MODEL,
)


class GeminiProvider(LLMProvider):

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=LLM_MODEL,
            google_api_key=GOOGLE_API_KEY,
            temperature=0.3,
        )

    async def generate(
        self,
        prompt: str
    ) -> str:

        print("Calling Gemini...")

        try:
            print("Calling Gemini...")

            response = await self.llm.ainvoke(prompt)

            print("Gemini Success")

            return response.content

        except Exception as e:

            print("Gemini Error:", repr(e))

            raise

        print("Gemini Response Received")

        return response.content


class LLMService:

    def __init__(self):

        provider = GeminiProvider()

        self.manager = LLMManager(provider)

    async def generate(
        self,
        prompt: str
    ) -> str:

        return await self.manager.generate(prompt)