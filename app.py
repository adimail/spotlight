import streamlit as st
from modules import extract
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs")
    st.header("Chat with multiple PDFs")
    st.text_input("Ask a question about your document")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDFs here", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                #Get PDF text
                raw_text = extract.get_pdf_text(pdf_docs)
                # st.write(raw_text)

                #Get PDF chunks
                text_chunks = extract.get_text_chunks(raw_text)
                # st.write(text_chunks)

                #Create vector storage
            

if __name__ == "__main__":
    main()