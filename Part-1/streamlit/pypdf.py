import streamlit as st
from streamlit.components.v1 import html
import requests
import PyPDF2
import os

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

# Streamlit UI
st.title("PDF Analyzer")

# Input for the PDF link
pdf_link = st.text_input("Enter the PDF link:")
analyze_button = st.button("Analyze")

if analyze_button and pdf_link:
    try:
        # Generate a unique filename based on the PDF link
        file_name = pdf_link.split("/")[-1]
        st.info(f"Analyzing {file_name}...")

        # Download the PDF
        download_pdf(pdf_link, file_name)


        # Analyze the downloaded PDF
        st.header("PDF Analysis")
        st.subheader("Text Extraction")

        text = extract_text_from_pdf(file_name)
        st.write(text)

        os.remove(file_name)



    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


