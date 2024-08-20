import PyPDF2

def add_metadata(input_file, output_file, title, author):
    pdf_reader = PyPDF2.PdfReader(input_file)
    pdf_writer = PyPDF2.PdfWriter()
    
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
     
    metadata = {
        '/Title' : title,
        '/Author' : author
    } 
    
    pdf_writer.add_metadata(metadata)
    
    with open(output_file, 'wb') as out:
        pdf_writer.write(out)
        
    print(f"PDF file with updated metadata is saved as {output_file}")        
    
add_metadata('merged.pdf', 'metadata_added.pdf', 'Sample for python Coding', 'Mohammadamin')    