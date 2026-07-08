from utils.chatbot import get_llm

llm = get_llm()

response = llm.invoke("Say hello!")

print(response.content)