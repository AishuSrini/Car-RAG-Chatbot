import uuid
from langchain import hub
from langchain_openai import AzureChatOpenAI
from langchain_community.document_loaders import AzureAIDocumentIntelligenceLoader
from langchain_openai import AzureOpenAIEmbeddings
from langchain.schema import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.text_splitter import MarkdownHeaderTextSplitter

# from langchain.vectorstores.azuresearch import AzureSearch
from langchain_community.vectorstores import AzureSearch
from langchain.schema import Document

from embeddings import setup_embeddings_model


def initialize_vector_store(embeddings_model):
    from config import (
        SEARCH_SERVICE_ENDPOINT,
        SEARCH_SERVICE_KEY,
        INDEX_NAME1,
    )

    embeddings_model: AzureOpenAIEmbeddings = setup_embeddings_model()

    INDEX_NAME12: str = INDEX_NAME1

    # Initialize the vector store
    vector_store: AzureSearch = AzureSearch(
        azure_search_endpoint=SEARCH_SERVICE_ENDPOINT,
        azure_search_key=SEARCH_SERVICE_KEY,
        index_name=INDEX_NAME12,
        embedding_function=embeddings_model.embed_query,
    )

    return vector_store


def add_embeddings_to_vector_store(vector_store: AzureSearch, embeddings, text_chunks):
    from config import (
        SEARCH_SERVICE_ENDPOINT,
        SEARCH_SERVICE_KEY,
        INDEX_NAME,
    )

    docs = []
    for idx, chunk in enumerate(text_chunks):
        doc = Document(
            page_content=chunk,  # Main content to index
            metadata={
                "id": str(uuid.uuid4()),  # Unique identifier for each document
                "chunk_id": str(idx),  # Any additional metadata
            },
        )
        docs.append(doc)

    vector_store.add_documents(documents=docs)


def get_retriever(vector_store: AzureSearch):
    # retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    retriever = vector_store.as_retriever(
        search_type="similarity", k=8, search_kwargs={"filter": ""}
    )
    return retriever
