from utils.pdf_loader import load_pdf

documents = load_pdf("data/dsa.pdf")

print(f"Total Pages: {len(documents)}")

print("\nFirst Page:\n")
print(documents[0].page_content)