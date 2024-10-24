from langchain.text_splitter import RecursiveCharacterTextSplitter

# Read the contents of the cleaned text file
with open("cleaned_car_manual.txt", "r", encoding="utf-8") as f:
    cleaned_text = f.read()

# # Assuming 'cleaned_text' is your variable containing the cleaned text
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,  # Adjust the size as needed
#     chunk_overlap=50,
# )

# texts = text_splitter.split_text(cleaned_text)
# print(f"Number of text chunks: {len(texts)}")


def split_text_into_chunks(cleaned_text, chunk_size=500, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return text_splitter.split_text(cleaned_text)
    print(f"Total chunks created: {len(text_splitter)}")
