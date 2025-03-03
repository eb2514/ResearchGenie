

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
import os
import time
import chromadb
import base64
import streamlit as st



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

def create_response(unique_results):
    response = ""
    for document in unique_results:    
        file_path = document.metadata['source']
        #llm = ChatOllama(model="llama3.2:3b")
        #result = llm.invoke(f"Summarize this in 100 words or less in bullet points with a newline after each, do not include introduction: {document.page_content}")
        with open(file_path, "rb") as file:
            file_bytes = file.read() 
            pdf_base64 = base64.b64encode(file_bytes).decode("utf-8")  
            #response += f"""  \n *{result.content}*  \n <iframe src="data:application/pdf;base64,{pdf_base64}#page={document.metadata["page"]}" width="80%" height="1000px"></iframe>  \n """
            response += f"""  \n <iframe src="data:application/pdf;base64,{pdf_base64}#page={document.metadata["page"]}" width="80%" height="1000px"></iframe>  \n """
    return response
    
def query_chroma(query):
    # Initialize the Chroma store
    embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("Communicating with server")
    client = chromadb.HttpClient(host=st.secrets['IP_ADDRESS'], port=8000)
    print("Communicating with server")
    chroma_store = Chroma(client=client, embedding_function=embedding_model, collection_name="my_collection")
    print("Communicating with server")

    # Query the database
    print(f"Querying for: '{query}'")
    results = chroma_store.similarity_search(query, k=3)
    unique_results = remove_duplicate_results(results)
    response = create_response(unique_results)
    #unique_results = ["A","B"]
    return response
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
