# app.py

import os
from data_extraction import extract_text_from_pdf, clean_text
from text_processing import split_text_into_chunks
from embeddings import setup_embeddings_model, generate_embeddings
from vector_store import (
    initialize_vector_store,
    add_embeddings_to_vector_store,
    get_retriever,
)
from chatbot import initialize_language_model, create_qa_chain, get_response


def main():
    # Step 1: Extract and Clean Text
    pdf_path = os.path.join("data", "User Manual.pdf")
    print(f"Opening PDF file at: {pdf_path}")
    print(f"Current working directory: {os.getcwd()}")

    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)
    print("Text extraction and cleaning completed.")

    # Step 2: Split Text into Chunks
    from config import CHUNK_SIZE, CHUNK_OVERLAP

    text_chunks = split_text_into_chunks(cleaned_text, CHUNK_SIZE, CHUNK_OVERLAP)
    print(f"Text split into {len(text_chunks)} chunks.")

    # Step 3: Generate Embeddings
    embeddings_model = setup_embeddings_model()
    embeddings = generate_embeddings(text_chunks, embeddings_model)
    print(f"Generated embeddings for {len(embeddings)} text chunks.")

    # Step 4: Initialize Vector Store and Add Embeddings
    vector_store = initialize_vector_store(embeddings_model)
    add_embeddings_to_vector_store(vector_store, embeddings, text_chunks)
    print("Embeddings added to vector store.")

    # Step 5: Set Up the Chatbot
    retriever = get_retriever(vector_store)
    llm = initialize_language_model()
    qa_chain = create_qa_chain(llm, retriever)
    print("Chatbot initialized and ready.")

    # Step 6: Interact with the User
    print(
        "You can now start interacting with the chatbot. Type 'exit' or 'quit' to stop."
    )

    while True:
        query = input("User: ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting the chatbot. Goodbye!")
            break
        result = get_response(qa_chain, query)
        print("Assistant:", result)


if __name__ == "__main__":
    main()
