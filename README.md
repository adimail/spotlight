# spotlight

# Language Model For Law - LLM
## SIH Project 2023 - Team Spotlight

The project address the significant challenge of providing accessible legal information and awareness to a large portion of India's population, particularly those lacking literacy or belonging to marginalized communities. It aims to achieve this by extracting text data from official Indian government legal documents, storing it in a vector database, and utilizing it to train a Large Language Model for Law (LLM). This LLM will serve as the foundation for a user-friendly chatbot designed to respond to legal-related queries and prompts. The project will rely on advanced Natural Language Processing (NLP) and Machine Learning (ML) techniques, as well as multilingual capabilities, to empower citizens with reliable and easily accessible legal information. Leveraging AI models like GPT-3.5 Turbo and Ada v2, along with Google Cloud Translation AI and Text-To-Speech (TTS) technology, this initiative aims to bridge the information gap for marginalized communities and individuals with low literacy levels in India.

## How it works

How It Works:

The project first reads the PDF documents and efficiently breaks down the text into manageable chunks. These text segments are then converted into vector representations using OpenAI embeddings, allowing for efficient data handling. When a user poses a legal query, the application utilizes semantic analysis to identify text chunks within the documents that are most relevant to the user's question. These contextually appropriate chunks are then fed into the Large Language Model for Law (LLM) to generate a comprehensive and accurate response.

The application uses Streamlit to create the GUI and Langchain to deal with the LLM.


## Installation

To install the repository, please clone this repository and install the requirements:

```
pip install -r requirements.txt
```

You will also need to add your OpenAI API key to the `.env` file.

## Usage

To use the application, run the `main.py` file with the streamlit CLI (after having installed streamlit): 

```
streamlit run app.py
```
