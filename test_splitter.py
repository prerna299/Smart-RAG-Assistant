from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents

documents = load_pdf("data/dsa.pdf")

chunks = split_documents(documents)

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0].page_content)