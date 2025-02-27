from langchain_community.document_loaders import PyMuPDFLoader
from concurrent.futures import ThreadPoolExecutor, as_completed
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
import os
import time


def process_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()
    return documents


# Function to embed and store documents in Chroma
def embed_and_store(documents, embedding, chroma_store):
    #print(documents)
    texts = [doc.page_content for doc in documents]
    metadatas = [doc.metadata for doc in documents]
    chroma_store.add_texts(texts=texts, metadatas=metadatas)

# Main ingestion function
def ingest(pdf_directory, chroma_db_path):
    # List all PDF files
    pdf_files = [os.path.join(pdf_directory, f) for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

    # Initialize progress tracking for PDF loading
    print("Processing PDFs...")
    total_files = len(pdf_files)
    completed_files = 0
    all_documents = []

    with ThreadPoolExecutor(max_workers=8) as executor:  # Adjust thread count for your system
        futures = {executor.submit(process_pdf, pdf_file): pdf_file for pdf_file in pdf_files}
        for future in as_completed(futures):
            try:
                documents = future.result()
                all_documents.extend(documents)
                completed_files += 1
                print(f"[{completed_files}/{total_files}] PDFs processed.")
            except Exception as e:
                print(f"Error processing file: {futures[future]} - {e}")

    # Initialize ChromaDB and embeddings
    embedding = FastEmbedEmbeddings()  # Replace with your FastEmbedEmbeddings implementation
    chroma_store = Chroma(persist_directory=chroma_db_path, embedding_function=embedding, collection_name="my_collection")

    # Embedding and storing progress
    print("Embedding and storing documents...")
    total_batches = (len(all_documents) + 999) // 1000  # Compute total batches
    completed_batches = 0
    batch_size = 1000

    for i in range(0, len(all_documents), batch_size):
        batch_docs = all_documents[i:i + batch_size]
        embed_and_store(batch_docs, embedding, chroma_store)
        completed_batches += 1
        print(f"[{completed_batches}/{total_batches}] Batches embedded and stored.")

    # Persist the database
    #chroma_store.persist()
    print(f"Ingested {total_files} PDFs into ChromaDB.")
    count = len(chroma_store.get()['ids']) if chroma_store.get() else 0
    if count == 0:
        print("Warning: The database is empty. Please run ingest() first.")


# Usage
# start = time.time()
ingest(pdf_directory="data", chroma_db_path="chroma_db") #"C://Users/elayb/OneDrive/Desktop/Pubmed"
# end = time.time()
# print(end-start)

def query_chroma(query):
    # Initialize the Chroma store
    embedding = FastEmbedEmbeddings()  # Replace with your embedding class
    chroma_store = Chroma(persist_directory="chroma_db", embedding_function=embedding, collection_name="my_collection")

    # Query the database
    print(f"Querying for: '{query}'")
    results = chroma_store.similarity_search(query, k=3)
    return results
    # Display results
    # for i, result in enumerate(results, start=1):
    #     #print(results)
    #     print(f"\nResult {i}:")
    #     print("\n----------------------------\n")
    #     print(f"Page Content: {result.page_content}")
    #     print("\n----------------------------\n")
    #     print(f"Metadata: {result.metadata}")
    #     print("\n----------------------------\n")
    #     #print(f"{result.metadata['source']}, {result.metadata['page']}")

# Example query
#query_chroma(chroma_db_path="chroma_db_new", query="What are the side effects of Caffiene on Vision", top_k=2)