import PyPDF2
import os

def merge_pdfs(input_folder, output_pdf):
    
    if os.path.exists(output_pdf):
        os.remove(output_pdf)
        
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]
    
    pdf_files.sort()
    
    pdf_writer = PyPDF2.PdfWriter()
    
        
    
    pdf_writer = PyPDF2.PdfWriter()
    for pdf in pdf_files:
        
        with open(os.path.join(input_folder, pdf), 'rb') as file:
        
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num]) 
    
    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)
    
input_folder = 'pdf_files'
output_pdf = 'pdf_files/merged.pdf'   
    
merge_pdfs('input_folder', 'output_pdf')
    