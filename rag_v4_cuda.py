

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
import os
import time

def query_chroma(query):
    # Initialize the Chroma store
    embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2", 
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
