from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from utils.vector_store import create_vector_store

# Load PDF
documents = load_pdf("data/dsa.pdf")

# Split into chunks
chunks = split_documents(documents)

print("Chunks:", len(chunks))

# Create FAISS database
db = create_vector_store(chunks)

print("Vector Database Created Successfully!")