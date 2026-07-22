from typing import List


def chunk_text(text: str , window : int = 4, overlap : int = 2)-> List[List[str]]:
    words = text.split(" ")
    chunks = []
    step = window - overlap


    for i in range(0, len(words),step):
        chunks.append(words[i: i + window])

    return chunks


