from typing import List


class Chunker:
    def __init__(self, window: int = 4, overlap: int = 2):
        self.window = window
        self.overlap = overlap

    def chunk_text(self, text: str) -> List[List[str]]:
        words = text.split(" ")
        chunks = []
        step = self.window - self.overlap
        for i in range(0, len(words), step):
            chunks.append(words[i: i + self.window])

        return chunks
