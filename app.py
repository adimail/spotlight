import streamlit as st
from modules import extract
from dotenv import load_dotenv
from htmltemplate import css, bot_template, user_template


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with multiple PDFs :books:")
    user_question = st.text_input("Ask a question about your documents:")
    # if user_question:
    #     handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = extract.get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = extract.get_text_chunks(raw_text)

                # create vector store
                vectorstore = extract.get_vector_store(text_chunks)

                # create conversation chain
                st.session_state.conversation = extract.get_conversation_chain(
                    vectorstore)

if __name__ == "__main__":
    main()