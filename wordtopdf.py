import streamlit as st
from docx import Document
from fpdf import FPDF
import os

def convert_docx_to_pdf(docx_file, pdf_file):
    doc = Document(docx_file)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)
        pdf.ln()
    
    pdf.output(pdf_file)

def main():
    st.title("Word to PDF Converter")
    uploaded_file = st.file_uploader("Upload a Word Document", type=["docx"])
    
    if uploaded_file is not None:
        pdf_filename = "converted.pdf"
        convert_docx_to_pdf(uploaded_file, pdf_filename)
        
        with open(pdf_filename, "rb") as pdf_file:
            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name=pdf_filename,
                mime="application/pdf"
            )
        
        os.remove(pdf_filename)

if __name__ == "__main__":
    main()
