import math
from typing import List

import numpy as np


class Similarity:
    @staticmethod
    def dot(a: List[int], b: List[int]) -> int:
        result = 0
        for i, e in enumerate(a):
            result = result + (e * b[i])
        return result

    @staticmethod
    def dot_numpy(a: List[int], b: List[int]) -> int:
        a_np = np.array(a)
        b_np = np.array(b)
        return np.dot(a_np, b_np)

    @classmethod
    def magnitude(cls, a: List[int]) -> float:
        return math.sqrt(cls.dot_numpy(a, a))

    # takes two vectors and return HOW MUCH SIMULAR THEY ARE
    @classmethod
    def cosign(cls, a: List[int], b: List[int]) -> float:
        mag_a = cls.magnitude(a)
        mag_b = cls.magnitude(b)
        if mag_a == 0 or mag_b == 0:
            return 0
        return cls.dot_numpy(a, b) / (mag_a * mag_b)
