from typing import List

from indexing import Chunker
from embed import Embedder
from search import Similarity


# The full piplines
# Take a text -> chunk the text -> embed those text (turn them into vectors)
# take an other text -> embed it -> use cosign to see which one is closer to the text (retrival)

class Pipeline:
    def __init__(self, window: int = 4, overlap: int = 2):
        self.chunker = Chunker(window=window, overlap=overlap)
        self.embedder = Embedder()
        self.database = []

    def index(self, text: str):
        chunks = self.chunker.chunk_text(text)
        self.database = [
            {"id": i, "text": chunk, "vector": self.embedder.embed(chunk)}
            for i, chunk in enumerate(chunks)
        ]

    def search(self, query: str):
        query_vector = self.embedder.embed(query.split())
        results = []
        for item in self.database:
            results.append({
                "id": item["id"],
                "vector": item["vector"],
                "cosign simularity": float(Similarity.cosign(item["vector"], query_vector)),
            })
        return results


def main():
    text = "Hypertension raises the risk of stroke and heart failure. Hypertension of."
    query = "Hypertension the risk of"

    pipeline = Pipeline(window=4)
    pipeline.index(text)
    results = pipeline.search(query)

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
