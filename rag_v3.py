from langchain_community.document_loaders import PyMuPDFLoader
from concurrent.futures import ThreadPoolExecutor, as_completed
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
import os
import time

# Function to process a single PDF file
def process_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()
    return documents

# Function to embed and store documents in Chroma
def embed_and_store(documents, embedding, chroma_store):
    texts = [doc.page_content for doc in documents]
    metadatas = [doc.metadata for doc in documents]
    chroma_store.add_texts(texts=texts, metadatas=metadatas)

# Main ingestion function with batching
def ingest_batched(pdf_directory, chroma_db_path, batch_size=1000, max_workers=4):
    # List all PDF files
    pdf_files = [os.path.join(pdf_directory, f) for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

    # Initialize ChromaDB and embeddings
    embedding = FastEmbedEmbeddings()  # Replace with your FastEmbedEmbeddings implementation
    chroma_store = Chroma(persist_directory=chroma_db_path, embedding_function=embedding)

    # Process PDFs in batches
    total_files = len(pdf_files)
    print(f"Total PDFs to process: {total_files}")
    for batch_start in range(0, total_files, batch_size):
        batch_end = min(batch_start + batch_size, total_files)
        pdf_batch = pdf_files[batch_start:batch_end]
        print(f"Processing batch {batch_start // batch_size + 1}: {batch_start} to {batch_end}")

        # Concurrently process PDFs in the batch
        all_documents = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(process_pdf, pdf_file): pdf_file for pdf_file in pdf_batch}
            for future in as_completed(futures):
                try:
                    documents = future.result()
                    all_documents.extend(documents)
                except Exception as e:
                    print(f"Error processing file: {futures[future]} - {e}")

        # Embed and store the documents for this batch
        print(f"Embedding and storing batch {batch_start // batch_size + 1}")
        embed_and_store(all_documents, embedding, chroma_store)

    # Persist the database
    chroma_store.persist()
    print(f"Ingestion complete. All PDFs are stored in ChromaDB at {chroma_db_path}.")

# Usage
# start = time.time()
# ingest_batched(pdf_directory="data", chroma_db_path="chroma_db_new2", batch_size=1000, max_workers=8)
# end = time.time()
# print(end-start)


def query_chroma(query, chroma_db_path, top_k=5):
    # Initialize ChromaDB and embeddings
    embedding = FastEmbedEmbeddings()  # Same embedding function as used during ingestion
    chroma_store = Chroma(persist_directory=chroma_db_path, embedding_function=embedding)

    # Perform the query
    results = chroma_store.similarity_search(query, k=top_k)

    return results

query = "What are the  side effects of Caffiene on Vision"
results = query_chroma(query=query, chroma_db_path="chroma_db_new2", top_k=1)

# Display results
print(f"Results for query '{query}':")
print(results)