import PyPDF2
import os

def extract_text_from_pdf(filename):
    file_path = os.path.join('docs', filename)

    try:
        pdf_file = open(file_path, 'rb')
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return

    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    pdf_file.close()
    return text

def export_text_to_txt(pdf_filename):
    try:
        if not os.path.exists('texts'):
            os.makedirs('texts')
        
        txt_filename = os.path.splitext(pdf_filename)[0] + '.txt'

        txt_filepath = os.path.join('texts', txt_filename)

        with open(txt_filepath, 'w', encoding='utf-8') as txt_file:
            txt_file.write(extract_text_from_pdf(pdf_filename))
    except Exception as e:
        print(f"An error occurred while writing to '{txt_filename}': {str(e)}")


# if __name__ == "__main__":
#     pdf_files_to_process = ['fundamental_rights.pdf', 'indian_constitution.pdf']

#     for pdf_filename in pdf_files_to_process:
#         export_text_to_txt(pdf_filename)
#         print(f"Text extracted from '{pdf_filename}' and saved as '{pdf_filename}.txt' in the 'texts' folder.")