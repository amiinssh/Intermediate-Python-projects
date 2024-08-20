import pdfplumber


def extract_text(pdf_path, output_text_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"

        with open(output_text_path, "w") as f:
            f.write(full_text)
        print(f"Extracted text is saved as {output_text_path}")


extract_text("merged.pdf", "output.txt")
