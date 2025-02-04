import faiss
import numpy as np

# Load stored embeddings
with open("code_embeddings.json", "r", encoding="utf-8") as f:
    code_index = json.load(f)

# Convert to numpy array
embeddings = np.array([entry["embedding"] for entry in code_index]).astype("float32")

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "code_index.faiss")
