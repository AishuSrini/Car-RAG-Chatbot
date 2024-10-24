 # 🚗 **RAG Chatbot for Car User Manuals**

The RAG Chatbot for Car User Manuals is an implementation of Retrieval-Augmented Generation (RAG) using LangChain. This application is designed to answer user questions related to a car's user manual by leveraging pre-processed text from the manual. The chatbot extracts relevant sections from the manual to provide accurate, context-aware responses about car operations, maintenance, and troubleshooting.

# 🌟 **Features**

**PDF Text Extraction:** Extracts raw text from car user manuals in PDF format and cleans it for processing.

**Text Chunking:** Splits large bodies of text into manageable chunks to optimize embedding generation.

**Embedding Generation:** Uses a pre-trained language model to generate embeddings from the text chunks, facilitating efficient retrieval.

**Vector Store Integration:** Adds the embeddings to a vector store and sets up a retriever for querying relevant sections of the car manual.

**Question Answering Chain (QA Chain):** Utilizes LangChain to implement a QA system that retrieves relevant information from the vector store and generates accurate responses.

**Interactive Chat Interface:** Provides a command-line interface (CLI) for users to interact with the chatbot in real-time and ask questions about car functionalities and troubleshooting.
# **🛠️ Installation**
# **Clone the repository:**
```
git clone https://github.com/your-username/RAG-Chatbot-Car-Manual.git

cd RAG-Chatbot-Car-Manual
```
# **Install the dependencies:**
```
pip install -r requirements.txt
```
# **Configure your environment (Optional):**

You can adjust configurations such as chunk size and overlap in the config.py file:

# config.py

```
CHUNK_SIZE = 500  # Size of each text chunk
CHUNK_OVERLAP = 50  # Overlap between chunks
```
# **🖥️ Usage**
**1.Prepare the Car User Manual:** Place the PDF file of your car's user manual in the data/ directory. By default, the code looks for a file named User Manual.pdf. You can adjust this path in the app.py file.

**2.Run the Application:** Start the chatbot by running the following command:
```
python app.py
```

**3.Interact with the Chatbot:** The chatbot will load the car user manual, create embeddings, and set up the QA chain. You can then type questions to interact with the bot. For example:
```
User: How do I change a flat tire?
Assistant: [Bot Response Based on the Car Manual]
```
To exit the chatbot, type exit or quit.

# **🧠 How it Works**
**Text Extraction:** Uses a PDF parsing utility to extract text from the car user manual.

**Embedding Generation:** A pre-trained language model generates vector embeddings for the text chunks, which are used for retrieval.

**Retrieval Augmentation:** When the chatbot receives a question, it retrieves the most relevant sections of the car manual by comparing embeddings and uses that information to generate a context-aware response.

#  **🛠 Example Questions**

How to Adjust mirrors?

What is the correct use of seat belts?

How to prevent windshield defogger from operating improperly?

How do I replace a headlight bulb?

# **👥 Contributing**

Contributions to this project are welcome! To contribute, please follow these steps:

1.Fork the repository.

2.Create a new branch.

3.Make your changes.

4.Push your changes to your fork.

5.Submit a pull request.

# **📜 License**

This project is released under the MIT License.


