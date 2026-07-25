from typing import List, Optional


class Embedder:
    DEFAULT_VOCABULARY = ["Hypertension", "of", "sugar", "stroke"]

    def __init__(self, vocabulary: Optional[List[str]] = None):
        self._vocabulary: List[str] = list(vocabulary) if vocabulary is not None else list(self.DEFAULT_VOCABULARY)
        self.len = len(self._vocabulary)

    @property
    def vocabulary(self) -> List[str]:
        return self._vocabulary

    def add_word(self, item: str):
        self._vocabulary.append(item)
        self.len = self.len + 1

    def delete_word(self, item: str):
        if item is not None and item in self._vocabulary:
            self._vocabulary.remove(item)
            self.len = self.len - 1
        else:
            print(f"Warning:'{item}' not found in vocabulary.")

    def modify_word(self, item: str, replacement: str):
        if item is not None and replacement is not None:
            if item in self._vocabulary:
                self.delete_word(item)
                self.add_word(replacement)
        else:
            print(f"Warning: None value.")

    def embed(self, chunk) -> List[int]:
        if isinstance(chunk, str):
            chunk = chunk.split()

        return [chunk.count(word) for word in self._vocabulary]
