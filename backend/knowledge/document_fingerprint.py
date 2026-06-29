import hashlib


class DocumentFingerprint:

    @staticmethod
    def generate(content: str):

        return hashlib.sha256(
            content.encode("utf-8")
        ).hexdigest()