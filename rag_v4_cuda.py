from langchain_community.document_loaders import PyMuPDFLoader
from concurrent.futures import ThreadPoolExecutor, as_completed
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
import os
import time


def process_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()
    return documents


# Function to embed and store documents in Chroma
def embed_and_store(documents, embedding_model, chroma_store):
    #print(documents)
    texts = [doc.page_content for doc in documents]
    metadatas = [doc.metadata for doc in documents]
    embedding= embedding_model.embed_documents(texts)
    chroma_store.add_texts(texts=texts, metadatas=metadatas, embeddings=embedding)

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
    embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2", 
    model_kwargs={"device":"cuda"},
    encode_kwargs={"batch_size":128},
    show_progress= True  # Ensures the model runs on GPU
    )
    chroma_store = Chroma(persist_directory=chroma_db_path, embedding_function=embedding_model, collection_name="my_collection")

    # Embedding and storing progress
    print("Embedding and storing documents...")
    total_batches = (len(all_documents) + 999) // 1000  # Compute total batches
    completed_batches = 0
    batch_size = 1000

    for i in range(0, len(all_documents), batch_size):
        batch_docs = all_documents[i:i + batch_size]
        embed_and_store(batch_docs, embedding_model, chroma_store)
        completed_batches += 1
        print(f"[{completed_batches}/{total_batches}] Batches embedded and stored.")

    # Persist the database
    #chroma_store.persist()
    print(f"Ingested {total_files} PDFs into ChromaDB.")
    count = len(chroma_store.get()['ids']) if chroma_store.get() else 0
    if count == 0:
        print("Warning: The database is empty. Please run ingest() first.")


def remove_duplicate_results(results):
    unique_results = []
    seen = set()
    for result in results:
        # Use page_content as the key to check for duplicates.
        content = result.metadata['source'].strip()
        if content not in seen:
            seen.add(content)
            unique_results.append(result)
    return unique_results

def query_chroma(query):
    # Initialize the Chroma store
    embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2", 
    model_kwargs={"device":"cuda"}
    )
    chroma_store = Chroma(persist_directory="chroma_db_v4", embedding_function=embedding_model, collection_name="my_collection")

    # Query the database
    print(f"Querying for: '{query}'")
    results = chroma_store.similarity_search(query, k=3)
    unique_results = remove_duplicate_results(results)
    return unique_results
    # for i, result in enumerate(unique_results, start=1):
    #     #print(results)
    #     print(f"\nResult {i}:")
    #     print("\n----------------------------\n")
    #     print(f"Page Content: {result.page_content}")
    #     print("\n----------------------------\n")
    #     print(f"Metadata: {result.metadata}")
    #     print("\n----------------------------\n")
    #     print(f"{result.metadata['source']}, {result.metadata['page']}")

# if __name__ == '__main__':
#     start = time.time()
#     #ingest(pdf_directory="C://Users/elayb/OneDrive/Desktop/Pubmed", chroma_db_path="chroma_db_v4")  #"C://Users/elayb/OneDrive/Desktop/Pubmed"
#     query_chroma(query="What are the side effects of Caffiene on Vision")
#     end = time.time()
    
#     print(end-start)

# Example query
#
