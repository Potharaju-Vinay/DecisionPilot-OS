import hashlib


class ResponseCache:

    def __init__(self):

        self.cache = {}

        self.hits = 0

        self.misses = 0

    def _hash(
        self,
        prompt: str
    ):

        return hashlib.sha256(
            prompt.encode()
        ).hexdigest()

    def get(
        self,
        prompt: str
    ):

        key = self._hash(prompt)

        if key in self.cache:

            self.hits += 1

            return self.cache[key]

        self.misses += 1

        return None

    def set(
        self,
        prompt: str,
        response: str
    ):

        key = self._hash(prompt)

        self.cache[key] = response

    def stats(self):

        return {

            "hits": self.hits,

            "misses": self.misses,

            "entries": len(self.cache)

        }