from sentence_transformers import SentenceTransformer
import json

# Load pre-trained model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Load extracted code index
with open("code_index.json", "r", encoding="utf-8") as f:
    code_index = json.load(f)

# Convert code components into vector embeddings
for entry in code_index:
    text = f"{entry['name']} - {entry['type']}\nDocstring: {entry['docstring'] or ''}"
    entry["embedding"] = model.encode(text).tolist()

# Save embeddings
with open("code_embeddings.json", "w", encoding="utf-8") as f:
    json.dump(code_index, f, indent=4)
