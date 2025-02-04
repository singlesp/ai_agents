import os
import ast
import json

def extract_code_components(repo_path):
    code_index = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):  # Adjust for other languages
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        tree = ast.parse(f.read(), filename=file_path)
                        for node in ast.walk(tree):
                            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                                code_index.append({
                                    "name": node.name,
                                    "type": "function" if isinstance(node, ast.FunctionDef) else "class",
                                    "file": file_path,
                                    "line": node.lineno,
                                    "docstring": ast.get_docstring(node),
                                })
                    except SyntaxError:
                        continue  # Skip files that can’t be parsed

    return code_index

repo_path = "path/to/your/repo"
index = extract_code_components(repo_path)

# Save index as JSON for later retrieval
with open("code_index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, indent=4)
