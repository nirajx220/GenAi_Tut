from pathlib import Path
from langchain.community.document_loaders import PyPDFLoader
pdf_path = Path(__file__).parent / "data" / "pdfs"

loaders = [PyPDFLoader(str(path)) for path in pdf_path.glob("*.pdf")]
docs = [doc for loader in loaders for doc in loader.load()]

print(f"Loaded {len(docs)} documents from {pdf_path}")