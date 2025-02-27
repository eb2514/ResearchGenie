from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import threading


def ingest():
    # Get the doc
    loader = PyPDFDirectoryLoader("data")
    #loader = PyPDFDirectoryLoader("data/10.1177_2473011424S00219.PMC11664715.pdf")
    pages = loader.load_and_split()
    # Split the pages by char
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(pages)
    print(f"Split {len(pages)} documents into {len(chunks)} chunks.")
    #
    embedding = FastEmbedEmbeddings()
    #Create vector store
    Chroma.from_documents(documents=chunks,  embedding=embedding, persist_directory="chroma_db")

def rag_chain():
    model = ChatOllama(model="llama3.2:3b")
    #
    prompt = PromptTemplate.from_template(
        """
        <s> [Instructions] Answer the question based only on the following context.
        If you don't know the answer, then reply, No Context available for this question {input}. [/Instructions] </s> 
        [Instructions] Question: {input} 
        Context: {context} 
        Answer: [/Instructions]
        """
    )
     
    #Load vector store
    embedding = FastEmbedEmbeddings()
    vector_store = Chroma(persist_directory="chroma_db", embedding_function=embedding)
    #Create chain
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 2,
            "score_threshold": 0.5,
        },
    )
    
    document_chain = create_stuff_documents_chain(model, prompt)
    chain = create_retrieval_chain(retriever, document_chain)
    return chain

def ask(query: str):
    #
    chain = rag_chain()
    # invoke chain
    result = chain.invoke({"input": query})
    # print results
    #print(result)
    for doc in result["context"]:
        print(f"Source: '{doc.metadata["source"]}#page={doc.metadata["page"]}'")

def get_query(query):
    result_dict = {"result": None}
    print(f"In get_query with {query}")
    def background_task():
        chain = rag_chain()
        result = chain.invoke({"input": query})
        result_dict["result"] = result

    thread = threading.Thread(target=background_task)
    thread.start()
    thread.join()
    #result = chain.invoke({"input": query})
    print("NNNNNNNNNOOOOOOOOWWWWWWWW EHRHERE")
    return result_dict["result"]


#ingest()
ask("How does Caffiene Effect vision?")





    # #response = query_rag(prompt)
    # with st.spinner("Searching..."):
    #     query = executor.submit(get_query(prompt))
    #     for doc in query["context"]:
    #         response = f"Source: {doc.metadata["source"]}#page={doc.metadata["page"]}"
    #         yield response  