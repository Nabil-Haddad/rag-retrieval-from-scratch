import numpy as np
from typing import List
import math

def dot(a:List[int], b:List[int])->int:
    result = 0
    for i, e in enumerate(a):
        result = result + (e * b[i])
    return result

def dot_numpy(a:List[int], b:List[int])->int:
    a_np = np.array(a)
    b_np = np.array(b)
    return np.dot(a_np, b_np)


def magnitude(a:List[int])->float:
    return math.sqrt(dot_numpy(a, a))

# takes two vectors and return HOW MUCH SIMULAR THEY ARE
def cosign(a:List[int], b: List[int])-> float:
    if magnitude(a) == 0 or magnitude(b) == 0:
        return 0
    return dot_numpy(a, b)/ (magnitude(a) * magnitude(b) )


vector_1 = [1, 0, 0, 1]
vector_2 = [0, 0, 0, 1]

#print(dot_numpy(vector_1,vector_2))
#print(magnitude([1,0,0,1]))
#print(cosign(vector_1, vector_2))
