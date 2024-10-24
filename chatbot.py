# chat.py
from langchain import hub
from langchain_community.chat_models import AzureChatOpenAI
from langchain_community.vectorstores import AzureSearch
from azure.core.credentials import AzureKeyCredential
from langchain_community.retrievers import AzureAISearchRetriever
from langchain_core.retrievers import BaseRetriever
from langchain.schema import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import AzureChatOpenAI
from langchain.chains.question_answering import load_qa_chain


def initialize_language_model():
    from config import (
        AZURE_OPENAI_API_KEY,
        AZURE_OPENAI_ENDPOINT,
        AZURE_OPENAI_API_VERSION,
        AZURE_OPENAI_API_VERSION_CHAT,
        CHAT_DEPLOYMENT,
    )

    llm = AzureChatOpenAI(
        deployment_name=CHAT_DEPLOYMENT,
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version=AZURE_OPENAI_API_VERSION_CHAT,
    )
    return llm


def initialize_retriever():
    from config import (
        SEARCH_SERVICE_ENDPOINT,
        SEARCH_SERVICE_KEY,
        INDEX_NAME,
        SEARCH_SERVICE_NAME,
    )

    # Initialize Azure Search vector store
    credential = AzureKeyCredential(SEARCH_SERVICE_KEY)
    vector_store: AzureSearch = AzureSearch(
        azure_search_endpoint=SEARCH_SERVICE_ENDPOINT,
        azure_search_key=credential,
        index_name=INDEX_NAME,
        embedding_function=None,  # You can pass a specific embedding function if needed
    )


retriever = AzureAISearchRetriever(
    content_key="content",
    top_k=1,
    index_name="cars-manual-index",
    service_name="SEARCH_SERVICE_NAME",
    api_key="SEARCH_SERVICE_KEY",
)


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


prompt = hub.pull("rlm/rag-prompt")


def create_qa_chain(llm, retriever):
    qa_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return qa_chain


def get_response(qa_chain, query):
    result = qa_chain.invoke(query)
    print("Assistant Answer:", result)
    return result
