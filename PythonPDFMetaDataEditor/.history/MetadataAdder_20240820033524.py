import PyPDF2

def add_metadata(input_file, output_file, title, author):
    pdf_reader = PyPDF2.PdfReader(input_file)
    pdf_writer = PyPDF2.PdfWiter()
    
    for page_num in range(len(pdf_reader.pages)):
        
     