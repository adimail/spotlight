# Spotlight

# Language Law Model - LLM
## SIH Project 2023 - Team Spotlight

This project addresses the challenge of providing accessible legal information and awareness to a significant portion of India's population, particularly those with limited literacy skills or belonging to marginalized communities. Our goal is to achieve this by extracting text data from official Indian government legal documents, storing it in a vector database, and utilizing it to train a Large Language Model for Law (LLM). This LLM will serve as the foundation for a user-friendly chatbot designed to respond to legal-related queries and prompts. Our project relies on advanced Natural Language Processing (NLP) and Machine Learning (ML) techniques, as well as multilingual capabilities, to empower citizens with reliable and easily accessible legal information. We leverage AI models such as GPT-3.5 Turbo and Ada v2, in addition to Google Cloud Translation AI and Text-To-Speech (TTS) technology. This initiative aims to bridge the information gap for marginalized communities and individuals with low literacy levels in India.

## How it works

### Project Workflow:

1. **Data Extraction:** We start by reading PDF documents and efficiently breaking down the text into manageable chunks.

2. **Vectorization:** These text segments are then converted into vector representations using OpenAI embeddings, allowing for efficient data handling.

3. **Semantic Analysis:** When a user poses a legal query, our application utilizes semantic analysis to identify text chunks within the documents that are most relevant to the user's question.

4. **Response Generation:** Contextually appropriate chunks are then fed into the Large Language Model for Law (LLM) to generate a comprehensive and accurate response.

## Running the Django Development Server

To run your Django project locally, you can use the built-in development server provided by Django. Follow these steps:

**1. Activate Your Virtual Environment (if applicable):**

If you're using a virtual environment (recommended), activate it. Replace `<env_name>` with the name of your virtual environment.

**2. Run the Development Server:**

Run the following command to start the Django development server:


By default, the server will run on `http://127.0.0.1:8000/`. You can access your Django project in your web browser by opening this URL.

**3. Access Your Django Application:**

Open your web browser and visit `http://127.0.0.1:8000/` (or the specified address if you changed the port). You should see your Django application up and running.

**4. Quit the Development Server:**

To stop the development server, press `CTRL-C` in the terminal where the server is running. Confirm that you want to quit the server when prompted.

That's it! You can now develop and test your Django application locally using the built-in development server.
