# embeddings.py

from langchain_openai.embeddings import AzureOpenAIEmbeddings
from langchain_community.embeddings import AzureOpenAIEmbeddings
import os


def setup_embeddings_model():
    from config import (
        AZURE_OPENAI_API_TYPE,
        AZURE_OPENAI_ENDPOINT,
        AZURE_OPENAI_API_KEY,
        AZURE_OPENAI_API_VERSION,
        EMBEDDINGS_DEPLOYMENT,
    )

    os.environ["AZURE_OPENAI_API_TYPE"] = AZURE_OPENAI_API_TYPE
    os.environ["AZURE_OPENAI_ENDPOINT"] = AZURE_OPENAI_ENDPOINT
    os.environ["AZURE_OPENAI_API_KEY"] = AZURE_OPENAI_API_KEY
    os.environ["AZURE_OPENAI_API_VERSION"] = AZURE_OPENAI_API_VERSION

    embeddings_model = AzureOpenAIEmbeddings(
        deployment=EMBEDDINGS_DEPLOYMENT,
        model="text-embedding-3-small",
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        chunk_size=500,
    )
    return embeddings_model


def generate_embeddings(text_chunks, embeddings_model):
    # Generate embeddings for each text chunk
    embeddings_model: AzureOpenAIEmbeddings = setup_embeddings_model()
    embeddings = embeddings_model.embed_documents(text_chunks)
    return embeddings
