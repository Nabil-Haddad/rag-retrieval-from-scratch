from typing import List
from indexing import chunk_text


sentence = "blood pressure blood"

def embedder(sentence)-> List[int]:
    vocabulary = ["Hypertension", "of", "sugar", "stroke"]
    if isinstance(sentence, str):
        sentence = sentence.split()
    
    vector = []

    for v in vocabulary:
        # see how many times v appeard in words 
        i = sentence.count(v)
        # append the value to vector
        vector.append(i)

    return vector




results = chunk_text(text = "Hypertension raises the risk of stroke and heart failure. Hypertension of." , window= 4)

#for result in results:
#    print(embedder(result))

a = embedder("Hypertension raises stroke risk")
b = embedder("high blood pressure increases stroke risk")
#print(a)
#print(b)
