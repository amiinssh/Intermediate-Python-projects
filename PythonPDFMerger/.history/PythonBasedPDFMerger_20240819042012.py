import PyPDF2

def merge_pdfs(pdf_list, output_path):
    pdf_writer = PyPDF2.PdfWriter()
    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
           pdf_writer.add_pages(pdf_reader.pages[page_num]) 
    
    with open(output_path, 'wb') as out:
        pdf_writer.write(out)
    print(f"Merged PDF saved as {output_path}")    
    
merge_pdfs('Page 1.pdf', 'Page 2.')    