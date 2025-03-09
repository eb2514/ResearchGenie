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
from openrouter import get_response



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
    crafted_response=[]
    pdf_list = []
    response = ""
    send_context =""
    file_endpoint = f"{st.secrets['file_endpoint']}"
    add_headers = {'ngrok-skip-browser-warning': "1"}
    for document in unique_results:
        file_path = document.metadata['source']
        send_context += document.page_content
        send_context += "\n <----------DELIMITER----------> \n"
        file_name = os.path.basename(file_path).replace("Pubmed",'').replace('\\', '/')
        file_url = f'{file_endpoint}{file_name}'
        get_request = requests.get(file_url, add_headers)
        if get_request.status_code == 200:
            pdf = requests.get(file_url)
            pdf_list.append(pdf)
            # pdf_viewer(pdf.content, height=800, width=600, resolution_boost=2)
            # st.write(file_url)
    response += get_response(send_context)
    response = response.split("<----------DELIMITER---------->")
    for i in range(0,len(response)+len(unique_results), 2):
        try:
            crafted_response.append(response[i])
            crafted_response.append(pdf_list[i])
        except IndexError:
            break
    return crafted_response
    
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
    results = chroma_store.similarity_search(query, k=2)
    unique_results = remove_duplicate_results(results)
    response = create_response(unique_results)
    return response
