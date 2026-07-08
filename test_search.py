from utils.vector_store import load_vector_store

db = load_vector_store()

query = "What is this PDF about?"

results = db.similarity_search(query, k=3)

print("Top Results:\n")

for i, doc in enumerate(results, start=1):
    print(f"----------- Result {i} -----------")
    print(doc.page_content)
    print()