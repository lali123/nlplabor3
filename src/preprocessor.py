import re
from typing import List

class TextCleaner:
    @staticmethod
    def clean(text: str) -> str:
        text = text.lower()
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        return text.strip()

    def batch_clean(self, texts: List[str]) -> List[str]:
        return [self.clean(t) for t in texts]
