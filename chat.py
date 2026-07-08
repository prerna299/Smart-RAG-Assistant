from utils.vector_store import load_vector_store
from utils.chatbot import get_llm

db = load_vector_store()
llm = get_llm()

while True:
    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    docs = db.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer ONLY from the given context.

Context:
{context}

Question:
{question}

If the answer is not in the context, say:
'I couldn't find the answer in the uploaded PDF.'
"""

    response = llm.invoke(prompt)

    print("\nAnswer:")
    print(response.content)