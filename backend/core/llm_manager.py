from backend.core.cache import ResponseCache
import asyncio


class LLMManager:

    def __init__(self, provider):

        self.provider = provider

        self.cache = ResponseCache()

    async def generate(
        self,
        prompt: str
    ):

        cached = self.cache.get(prompt)

        if cached:

            return cached

        retries = 3

        for attempt in range(retries):

            try:

                response = await self.provider.generate(prompt)

                self.cache.set(
                    prompt,
                    response
                )

                return response

            except Exception:

                if attempt == retries - 1:

                    raise

                await asyncio.sleep(2)