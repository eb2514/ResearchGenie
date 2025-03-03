

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
import os
import time
import chromadb
#import streamlit as st

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

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
    model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("Communicating with server")
    #client = chromadb.HttpClient(host=st.secrets['IP_ADDRESS'], port=8000)
    print("Communicating with server")
    #chroma_store = Chroma(client=client, embedding_function=embedding_model, collection_name="my_collection")
    print("Communicating with server")

    # Query the database
    print(f"Querying for: '{query}'")
    #results = chroma_store.similarity_search(query, k=3)
    #unique_results = remove_duplicate_results(results)
    unique_results = "A"
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
