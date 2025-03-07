__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
import base64
import requests
import os
import time
import chromadb
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer



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

# def create_response(unique_results):
#     response = ""
#     for document in unique_results:    
#         file_path = document.metadata['source']
#         llm = ChatOllama(model="llama3.2:3b")
#         result = llm.invoke(f"Summarize this in 100 words or less in bullet points with a newline after each, do not include introduction: {document.page_content}")
#         with open(file_path, "rb") as file:
#             file_bytes = file.read() 
#             pdf_base64 = base64.b64encode(file_bytes).decode("utf-8")  
#             response += f"""  \n *{result.content}*  \n <iframe src="data:application/pdf;base64,{pdf_base64}#page={document.metadata["page"]}" width="80%" height="1000px"></iframe>  \n """
#     return response

def create_response(unique_results):
    response = ""
    file_endpoint = f"{st.secrets['file_endpoint']}"
    add_headers = {'ngrok-skip-browser-warning': "1"}
    for document in unique_results:
        file_path = document.metadata['source']
        file_name = os.path.basename(file_path).replace("Pubmed",'').replace('\\', '/')
        file_url = f'{file_endpoint}{file_name}'
        #st.write(file_url)
        llm = ChatOllama(model="llama3.2:3b")
        ai_summarizer = llm.invoke(f"Summarize this in 100 words or less in bullet points with a newline after each, do not include introduction: {document.page_content}")
        st.write(ai_summarizer)
        get_request = requests.get(file_url, add_headers)
        if get_request.status_code == 200:
            pdf = requests.get(file_url)
            pdf_viewer(pdf.content, height=800, width=600, resolution_boost=2)
            #pdf_base64 = base64.b64encode(get_request.content).decode("utf-8")
            #response += f"""  \n <iframe src="data:application/pdf;base64,{pdf_base64}#page={document.metadata["page"]}" width="80%" height="1000px"></iframe>  \n """
            #response += f"""  \n <iframe src="https://806a-2607-fea8-3fb2-3800-71b7-4f42-4d2a-805f.ngrok-free.app/get_file/Pubmed/epj-10-6215.PMC5853996.pdf#page={document.metadata["page"]}" width="80%" height="1000px"></iframe>  \n """
            #response += f"""  \n {pdf.content}  \n """
            
    return response
    
def query_chroma(query):
    # Initialize the Chroma store
    embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("Communicating with server")
    client = chromadb.HttpClient(host=st.secrets['ADDRESS'], port=443, ssl=True)
    print("Communicating with server")
    chroma_store = Chroma(client=client, embedding_function=embedding_model, collection_name="my_collection")
    print("Communicating with server")

    # Query the database
    print(f"Querying for: '{query}'")
    results = chroma_store.similarity_search(query, k=1)
    unique_results = remove_duplicate_results(results)
    response = create_response(unique_results)
    return response
