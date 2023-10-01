import streamlit as st
import requests
import PyPDF2
import os
import subprocess

st.title("PDF Analyzer")

def download_pdf(pdf_url, save_path):
    response = requests.get(pdf_url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def pypdf_extract(pdf_path):
    text = ""
    pdf_file = open(pdf_path, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        text += page.extract_text()
    
    pdf_file.close()
    return text

def nougat_extract(pdf_path):
    path = pdf_path
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    print(pdf_name)
    # command = [
    #     "nougat",
    #     "--markdown",
    #     "pdf",
    #     path,
    #     "--out",
    #     ".",
    # ]

    with st.spinner("Processing..."):
        # Set the environment variable
        os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'

        # Run the nougat command
        subprocess.run(['nougat', '--markdown', path, 'f2.pdf', '--out', '.'], check=True)
        st.success("Process completed!")
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        file_contents = f'{pdf_name}.mmd'
        file = open(file_contents, 'r')
        return file.read()



def display(package, text_string):
    title = package
    text = text_string

    st.markdown(
        f'<h3>{title}</h3>'
        f'<div style="white-space: pre-wrap; border:1px solid #ccc; padding:10px; overflow:auto; width:1000px; height:500px;">'
        f'{text}'
        f'</div>', 
        unsafe_allow_html=True
    )


# Input for the PDF link
pdf_link = st.text_input("Enter the PDF link:")
analyze_button = st.button("Analyze")

if pdf_link and analyze_button:
    file_name = pdf_link.split("/")[-1]
    download_pdf(pdf_link, file_name)
    pypdf_text = pypdf_extract(file_name)
    display("PyPDF", pypdf_text)
    nougat_text = nougat_extract(file_name)
    display("Nougat", nougat_text)
try:
    if pdf_link:
        os.remove(file_name)
except:
    pass

