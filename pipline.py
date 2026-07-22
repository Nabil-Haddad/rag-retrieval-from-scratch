from typing import List
from indexing import chunk_text
from embed import embedder
from search import cosign


# The full piplines 
# Take a text -> chunk the text -> embed those text (turn them into vectors)
# take an other text -> embed it -> use cosign to see which one is closer to the text (retrival)

text = "Hypertension raises the risk of stroke and heart failure. Hypertension of."
test = "Hypertension the risk of"

def pipline():
    chunks = chunk_text(text = text , window= 4)
    database = []
    for i, chunk in enumerate(chunks):
        database.append({"id": i, "text": chunk, "vector" :embedder(chunk) })

    test_chunked = test.split()
    results = []

    for element in database:
        results.append({"id": element["id"], 
                        "vector": element["vector"],
                        "cosign simularity":float(cosign(element["vector"], embedder(test_chunked))) })


    for r in results:
        print(r)



if __name__ == "__main__":
    pipline()



