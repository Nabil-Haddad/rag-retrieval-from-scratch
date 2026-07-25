# vector-search-from-scratch

A minimal vector search engine built from scratch, chunking, hand-written embeddings, and
cosine similarity with no black-box libraries, to understand how RAG retrieval really works.

## Why this exists

Most retrieval tutorials hand you `model.encode()` and `db.query()` and call it a day. You end
up with something that runs but that you can't explain. I wanted the opposite: to build every
piece by hand, the chunker, the embedder, the similarity math, so that nothing in a real RAG
pipeline is a mystery. This repo is that build, done one line at a time and reasoned through
rather than copied.

It is deliberately small. The point isn't scale, it's understanding.

## What it does

It's the full retrieval loop that sits underneath every RAG system, implemented from nothing:

1. **Chunk** a document into overlapping windows of words (a sliding window).
2. **Embed** each chunk into a vector of numbers.
3. **Store** the chunks and their vectors.
4. **Search**: embed a query, then score every chunk by cosine similarity and rank them.

## The idea it demonstrates

The embedder here is intentionally primitive: it counts how often each word from a small
vocabulary appears in a chunk. That's a real embedding — text in, numbers out — but it has a
revealing limitation. Two sentences that *mean* the same thing but use different words come out
as very different vectors:

```
"Hypertension raises stroke risk" -> [1, 0, 0, 1]
"high blood pressure increases stroke risk" -> [0, 0, 0, 1]
```

A counting embedder can only see shared *words*, not shared *meaning* — so synonyms look like
strangers to it. That single limitation is the entire reason trained neural embeddings exist,
and building the naive version first makes that reason obvious instead of abstract.

## Structure

Each stage of the pipeline is its own class, so the pieces can be swapped independently
(a real embedder can replace `Embedder` without touching anything else).

| File | Class | What it holds |
|------|-------|----------------|
| `indexing.py` | `Chunker` | the sliding-window chunker (tunable window + overlap) |
| `embed.py` | `Embedder` | owns a vocabulary and turns a chunk into a count vector |
| `search.py` | `Similarity` | `dot()`, `magnitude()`, `cosign()` — cosine similarity, built up from the dot product |
| `pipline.py` | `Pipeline` | ties it together: chunk -> embed -> store -> query -> rank |

## Run it

```bash
python pipline.py
```

You'll see each chunk scored against a query by cosine similarity, and you'll spot the moments
where the tiny vocabulary can't tell chunks apart, which is exactly the wall a real embedder
removes.

## What's next

The whole pipeline is designed so only **one** piece needs to change to go from toy to real:
swap the counting `Embedder` for a trained neural embedder (e.g. `sentence-transformers`).
Everything else, chunking, storage, cosine similarity, stays exactly the same. That's the
next step for this repo.

---

*Built from scratch as a learning project, No Ai envolved.*