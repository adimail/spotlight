import streamlit as st
from modules import extract
from dotenv import load_dotenv
from htmltemplate import css, bot_template, user_template
import chainlit as cl

def main():
    load_dotenv()
    st.set_page_config(page_title="KYR")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("welcome to the know your rights framework")
    user_question = st.text_input("Ask a question about your uploaded documents:")
    if user_question:
        extract.handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your docs")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = extract.get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = extract.get_text_chunks(raw_text)
                st.write(text_chunks)

                # create vector store
                vectorstore = extract.get_vector_store(text_chunks)

                # create conversation chain
                st.session_state.conversation = extract.get_conversation_chain(vectorstore)


if __name__ == '__main__':
    main()
