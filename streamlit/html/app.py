from flask import Flask, render_template, request

from modules import extract

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    uploaded_files = request.files.getlist('pdf_docs')
    raw_text = extract.get_pdf_text(uploaded_files)
    text_chunks = extract.get_text_chunks(raw_text)
    vectorstore = extract.get_vector_store(text_chunks)
    conversation_chain = extract.get_conversation_chain(vectorstore)
    
    user_question = request.form['user_question']
    response = extract.handle_userinput(user_question, conversation_chain)

    return render_template('result.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
