import streamlit as st
import requests
import PyPDF2
import os
import subprocess

st.title("PDF Analyzer through PyPDF2 and Nougat")

def download_pdf(pdf_url, save_path):
    response = requests.get(pdf_url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_file = open(pdf_path, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        text += page.extract_text()
    
    pdf_file.close()
    return text

def nougat(pdf_path):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    command = [
        "nougat",
        "--markdown",
        "pdf",
        pdf_path,
        "--out",
        "input/",
    ]
    with st.spinner("Processing..."):
        subprocess.run(command, check=True)
        os.remove(pdf_path)
        st.success("Process completed!")
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        file_contents = f'input/{pdf_name}.mmd'
        file = open(file_contents, 'r')

        st.text("Nougat Summary:")
        st.code(file.read())

# Streamlit UI
col1, col2 = st.columns(2)

# Input for the PDF link
pdf_link = st.text_input("Enter the PDF link:")

option = st.selectbox(
    'Select the type of analysis',
    ('PyPDF2', 'Nougat')
)

if pdf_link:
    file_name = pdf_link.split("/")[-1]
    st.info(f"Analyzing {file_name}...")
    download_pdf(pdf_link, file_name)

# Apply custom styling to col1
with col1:
    if option == 'PyPDF2' and pdf_link:
        st.header("PDF Analysis")
        st.subheader("Text Extraction")
        text = extract_text_from_pdf(file_name)
        st.write(text)
    elif option == 'Nougat' and pdf_link:
        st.header("PDF Analysis")
        st.subheader("Text Extraction")
        nougat(file_name)

with col2:
    st.header("Summary of the PDF")
    st.write("Summary of the PDF will be displayed here")

# Clean up the temporary PDF file
if pdf_link:
    os.remove(file_name)
