import streamlit as st
import time
from rag_v4_cuda import query_chroma
from concurrent.futures import ThreadPoolExecutor
import base64
from langchain_community.chat_models import ChatOllama




st.markdown(
    """
    <style>
    /* Increase size of chat input */
    .st-emotion-cache-12cetgn .ekr3hml7 {
        font-size: 18px;  /* Adjust this to increase the text input size */
        height: 50px;     /* Adjust this to increase the input box height */
        width: 100%;
    }
        
        /* Increase size of chat messages */
    .stChatMessage .stMessage {
        font-size: 18px;  /* Adjust this to increase the message text size */
    }

        /* Customize chat message bubble size */
    .stChatMessage {
        padding: 12px 20px;  /* Increase padding for a larger message bubble */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def send_query(prompt):
    with st.spinner("Searching..."):
        query = query_chroma(prompt)
        #response = f"""**{query.page_content}**  \n """
        response =""
        for document in query:
            response += create_response(document)
        return response             

def create_response(document):
    #file_path = document.metadata['source']
    llm = ChatOllama(model="llama3.2:3b")
    #result = llm.invoke(f"Summarize this in 100 words or less in bullet points with a newline after each, do not include introduction: {document.page_content}")
    result = llm.invoke(f"Summarize this in 100 words or less in bullet points with a newline after each, do not include introduction: Chocolate chip cookie recipe")
    #with open(file_path, "rb") as file:
        #file_bytes = file.read() 
        #pdf_base64 = base64.b64encode(file_bytes).decode("utf-8")  
        #response = f"""  \n *{result.content}*  \n <iframe src="data:application/pdf;base64,{pdf_base64}#page={document.metadata["page"]}" width="80%" height="1000px"></iframe>  \n """
    response = f"""  \n *{result.content}*  \n " width="80%" height="1000px"></iframe>  \n """
    return response
    
if "chats" not in st.session_state:
    st.session_state.chats = {"Default Chat": []}
if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Default Chat"

if st.session_state.current_chat not in st.session_state.chats:
    st.session_state.current_chat = list(st.session_state.chats.keys())[0]

#####   SIDEBAR    #####
history, docs = st.sidebar.tabs(["Chat History", "Documents"])

#####   HISTORY TAB DONE    #####
history_tab = history.container(border=True)
docs_tab = docs.container(border=True)
dialog_box = st.empty()
with history_tab:
    col1, col2 = history_tab.columns([3,1])
    #Clicking chats
    with col1:
        for chat_name in list(st.session_state.chats.keys()):
            if col1.button(chat_name):
                st.session_state.current_chat = chat_name
            if col2.button("Delete", key=f"delete_{chat_name}"):
                if len(st.session_state.chats) > 1 and (chat_name != "Default Chat"):
                    del st.session_state.chats[chat_name]
                    st.rerun()
                else:
                    dialog_box.warning("Cannot delete default chat. Erasing chat instead.")
                    st.session_state.chats[st.session_state.current_chat] = []
                      # Delete the chat from session state
                # If the deleted chat was the current chat, switch to the first remaining chat
                    if st.session_state.current_chat == chat_name and st.session_state.chats:
                        st.session_state.current_chat = list(st.session_state.chats.keys())[0]
                

    #Creating new chats
    with col1:
        if new_chat_name := col1.chat_input("Add a new chat",key=f"add_{chat_name}" ):    
            if new_chat_name and new_chat_name not in st.session_state.chats:
                st.session_state.chats[new_chat_name] = []
                st.session_state.current_chat = new_chat_name
                st.rerun()

    # # Clear current chat history
    #     if history_tab.button("Clear Current Chat"):
    #         st.session_state.chats[st.session_state.current_chat] = []
with docs_tab:
    docs_tab.write("UNDER CONSTRUCTION :building_construction:")

#####   Main Chat Interface #####

main_chat = st.container(border=True)

with main_chat:

    main_chat.title("ResearchGenie :genie:", anchor="What is this?", help="What is this?")
    main_chat.caption(f"Chat: {st.session_state.current_chat}")
    main_chat.divider()
# Display chat history
chat_history = st.session_state.chats.get(st.session_state.current_chat, [])
for message in chat_history:
    if message["role"] == "user":
        st.chat_message(message['role']).markdown(message["content"], unsafe_allow_html=True)
    else:
        st.chat_message(message['role']).markdown(message["content"], unsafe_allow_html=True)

if prompt := st.chat_input("Search for something"):
    st.chat_message("user").markdown(prompt)
    st.session_state.chats[st.session_state.current_chat].append({"role":"user", "content":prompt})
    with st.chat_message("assistant"):
        response_text = send_query(prompt)
        st.markdown(response_text, unsafe_allow_html=True)
        st.session_state.chats[st.session_state.current_chat].append({"role": "assistant", "content": response_text})
        
#How does Caffeine Effect vision?
