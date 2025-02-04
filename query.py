def search_code(query, k=5):
    query_embedding = model.encode(query).astype("float32")

    # Load FAISS index
    index = faiss.read_index("code_index.faiss")

    # Search
    distances, indices = index.search(np.array([query_embedding]), k)

    # Retrieve matching functions/classes
    results = [code_index[i] for i in indices[0]]

    return results

query = "How do I load a dataset in this codebase?"
matches = search_code(query)

for match in matches:
    print(f"Found: {match['name']} in {match['file']} (line {match['line']})")
