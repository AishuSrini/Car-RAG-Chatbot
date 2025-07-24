# 🚗 **RAG Chatbot for Car User Manuals using Langchain 🦜🔗**

The RAG Chatbot for Car User Manuals project is an implementation of Retrieval-Augmented Generation (RAG) using LangChain. It leverages various services such as **Azure OpenAI models, Azure Search Service, and Python** to create an interactive chatbot that helps users query information from a car user manual. The chatbot extracts text from the manual, retrieves relevant sections based on user queries, and generates responses using advanced **AI models**.

# 🌟 **Features**

 🔧 **Python-based Application:** The chatbot is developed in Python, using libraries such as LangChain for natural language processing and question-answering tasks.
 
 🦜 **LangChain for QA Chain:** Implements LangChain to create a robust Question Answering (QA) system that generates relevant and accurate answers based on retrieved data.

📄 **PDF Text Extraction:** Extracts raw text from car user manuals in PDF format and cleans it for embedding and retrieval.

✂️  **Text Chunking:** Splits large sections of the car manual into smaller chunks to optimize the embedding process and improve retrieval accuracy.

🤖 **Azure OpenAI Models:** Uses Azure OpenAI models to generate embeddings from the text chunks, facilitating efficient retrieval leveraging embed models and answer user queries with context-aware, natural language responses using chat models.

🗃️ **Vector Store Integration:** Adds the generated embeddings to a vector store, which is integrated with **Azure Search Service**, allowing fast and relevant searches.

🔗 **Question Answering Chain (QA Chain):** Utilizes LangChain to implement a QA system that retrieves relevant information from the vector store and generates accurate responses.

 🗨️ **Interactive Chat Interface:** Provides a command-line interface (CLI) for users to interact with the chatbot in real-time and ask questions about car functionalities and troubleshooting.
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
# **Configure your environment :**
Azure OpenAI API Configuration:
Configure your Azure OpenAI API key in the config.py file:

```
OPENAI_API_KEY = 'your_azure_openai_api_key_here'
```
**Azure Search Service Configuration:**

Configure your Azure Search Service connection details in config.py:
```
AZURE_SEARCH_SERVICE_NAME = 'your_search_service_name'
AZURE_SEARCH_INDEX_NAME = 'your_search_index_name'
AZURE_SEARCH_ADMIN_KEY = 'your_admin_key_here'

```
You can also adjust configurations such as chunk size and overlap:

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
# 🤖 **Demo:**

**Watch a Demo Video:**
[Watch the demo on YouTube] https://youtu.be/-1WQW3VURrc
# **🧠 How it Works**
**Text Extraction:** Uses a PDF parsing utility to extract text from the car user manual.

**Embedding Generation:**  **Azure OpenAI models** are used to generate vector embeddings from the cleaned text chunks.

**Retrieval Augmentation:** The chatbot utilizes **Azure Search Service** to efficiently retrieve the most relevant sections of the car manual based on user queries. This allows the chatbot to search through large documents quickly and accurately.

**LangChain Integration:** LangChain is used to connect the retrieval system with the language model, enabling the chatbot to retrieve relevant data from the car manual based on user queries. The language model then uses this retrieved data to generate coherent and contextually relevant responses.
  
  ⛓️ **LangChain orchestrates** the process, ensuring the correct data is retrieved and fed into the language model.
  
   📝 **The prompt (provided to the language model)** ensures that the response is coherent and relevant to the user's question.

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

