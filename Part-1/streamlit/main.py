import logging
from cloudwatch import cloudwatch
import streamlit as st
import requests
import PyPDF2
import os
import subprocess
import spacy
import re
import time
import boto3

aws_region = 'us-east-1'
boto3.setup_default_session(region_name=aws_region)

logger = logging.getLogger('my_logger')
formatter = logging.Formatter('%(asctime)s : %(levelname)s - %(message)s')

handler = cloudwatch.CloudwatchHandler(
 log_group = 'Assignment-1-Part-1',
 log_stream = 'streamlit',
 access_id = st.secrets['AWS_ACCESS_KEY_ID'], 
 access_key = st.secrets['AWS_SECRET_ACCESS_KEY']
)

#Pass the formater to the handler
handler.setFormatter(formatter)
#Set the level
logger.setLevel(logging.INFO)
#Add the handler to the logger
logger.addHandler(handler)

st.title("PDF Analyzer")



def download_pdf(pdf_url, save_path):
    logger.info("Download PDF function is invoked")
    response = requests.get(pdf_url)
    with open(save_path, 'wb') as file:
        file.write(response.content)


def pypdf_extract(pdf_path):
    try:
        logger.info("PyPdf Extraction function is invoked")
        text = ""
        pdf_file = open(pdf_path, "rb")
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
        
        pdf_file.close()
        return text
    except:
        st.error("Something went wrong with PyPDF!")
        st.error("Please check the PDF link and try again!")
        logger.info("An error from PyPDF!")
        logger.info("pypdf_extract function is raising an error")
        os.remove(file_name)


def nougat_extract(pdf_path):
    try:
        logger.info("Nougat Extraction function is invoked")
        path = pdf_path
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        print(pdf_name)

        with st.spinner("Processing..."):
            os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'  # Use CPU if GPU not available
            subprocess.run(['nougat', '--markdown', 'pdf', path, '--out', '.'], check=True)
            st.success("Process completed!")
            pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
            file_contents = f'{pdf_name}.mmd'
            file = open(file_contents, 'r')
            os.remove(file_contents)
            return file.read()
    except:
        st.error("Something went wrong with Nougat!")
        st.error("Please check the PDF link and try again!")
        logger.info("An error from Nougat!")
        logger.info("nougat_extract function is raising an error")
        os.remove(file_name)


def display(package, text_string):
    try:
        logger.info("Display function is invoked")
        title = package
        st.markdown(f'<h3>{title}</h3>', unsafe_allow_html=True)
        st.markdown(
            f'<div style="white-space: pre-wrap; border:1px solid #ccc; padding:10px; overflow-y:scroll; width:100%; max-height:500px;">'
            f'{text_string}'
            f'</div>', 
            unsafe_allow_html=True
        )
    except:
        st.error("Something went wrong!")
        st.error("Please check the PDF link and try again!")
        logger.info("An error from display function")
        os.remove(file_name)


def summary(text):
    try:
        logger.info("Summary function is invoked")
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        sentences = list(doc.sents)
        urls = [token.text for token in doc if token.like_url]
        numbers = re.findall(r'\b\d+\b', text)
        num_numbers = len(numbers)  
        num_links = len(urls)
        num_sentences = len(sentences)
        num_words = len(doc)
        return [num_words, num_sentences, num_numbers, num_links]
    except:
        st.error("Something went wrong!")
        st.error("Please check the PDF link and try again!")
        logger.info("An error from summary function")
        os.remove(file_name)


def disp_summary(title, l, t):
    logger.info("Display Summary function is invoked")
    st.subheader(title)
    st.write(f"Words - {l[0]}")
    st.write(f"Sentences - {l[1]}")
    st.write(f"Number - {l[2]}")
    st.write(f"Links - {l[3]}")
    st.write(f"Execution Time - {t:.2f} seconds")

def generate_summary_text(l, t):
    logger.info("Generating Summary Text function is invoked")
    summary_text = (
        f"Words - {l[0]}\n"
        f"Sentences - {l[1]}\n"
        f"Number - {l[2]}\n"
        f"Links - {l[3]}\n"
        f"Execution Time - {t:.2f} seconds"
    )
    return summary_text


# Input for the PDF link
pdf_link = st.text_input("Enter the PDF link:")

#Choose the extraction method
extractor_choice = st.selectbox(
    "Choose an extraction method:",
    ["PyPdf", "Nougat", "Nougat and PyPdf"]
)

analyze_button = st.button("Analyze")
logger.info("Analyze button clicked")

try:
    if pdf_link and analyze_button:
        logger.info("PDF link and Analyze button clicked")
        file_name = pdf_link.split("/")[-1]
        download_pdf(pdf_link, file_name)


        if extractor_choice == 'PyPdf':
            logger.info("PyPdf Extraction is selected")
            start = time.time()
            logger.info("File is extracted and Downloaded from the link")
            pypdf_text = pypdf_extract(file_name)
            end = time.time()
            p_exec = end - start
            logger.info("PyPdf Extraction started")
            display("PyPDF", pypdf_text)
            logger.info("PyPdf Extraction completed")
            p_summary = summary(pypdf_text)
            disp_summary('PyPDF Summary', p_summary, p_exec)
            logger.info("PyPdf Summary completed")
            st.download_button(
                label="Download Extracted Data",
                data=pypdf_text,
                file_name="pypdf_extraction.txt"
            )
            st.download_button(
                label="Download Summary",
                data=generate_summary_text(p_summary, p_exec),
                file_name="pypdf_summary.txt"
            )
            os.remove(file_name)
            logger.info("File removed")



        if extractor_choice == 'Nougat':
            logger.info("Nougat Extraction is selected")
            start = time.time()
            logger.info("File is extracted and Downloaded from the link")
            nougat_text = nougat_extract(file_name)
            end = time.time()
            n_exec = end - start
            logger.info("Nougat Extraction started")
            display("Nougat", nougat_text)
            logger.info("Nougat Extraction completed")
            n_summary = summary(nougat_text)
            disp_summary('Nougat Summary', n_summary, n_exec)
            logger.info("Nougat Summary completed")
            st.download_button(
                label="Download Extracted Data",
                data=nougat_text,
                file_name="nougat_extraction.txt"
            )
            st.download_button(
                label="Download Summary",
                data=generate_summary_text(n_summary, n_exec),
                file_name="nougat_summary.txt"
            )
            os.remove(file_name)
            logger.info("File removed")


        if extractor_choice == 'Nougat and PyPdf':
            logger.info("Nougat and PyPdf Extraction is selected")
            col1, col2 = st.columns(2)
            start = time.time()
            logger.info("File is extracted and Downloaded from the link")
            nougat_text = nougat_extract(file_name)
            end = time.time()
            n_exec = end - start


            with col1:
                logger.info("Nougat Extraction started")
                display("Nougat", nougat_text)
                logger.info("Nougat Extraction completed")
                n_summary = summary(nougat_text)
                disp_summary('Nougat Summary', n_summary, n_exec)
                logger.info("Nougat Summary completed")
                st.download_button(
                    label="Download Nougat Extracted Data",
                    data=nougat_text,
                    file_name="nougat_extraction.txt"
                )
                logger.info("Nougat Extraction downloaded")
                st.download_button(
                    label="Download Nougat Summary",
                    data=generate_summary_text(n_summary, n_exec),
                    file_name="nougat_summary.txt"
                )
                logger.info("Nougat Summary downloaded")
            start = time.time()
            pypdf_text = pypdf_extract(file_name)
            end = time.time()
            p_exec = end - start


            with col2:
                logger.info("PyPdf Extraction started")
                display("PyPDF", pypdf_text)
                logger.info("PyPdf Extraction completed")
                p_summary = summary(pypdf_text)
                disp_summary('PyPDF Summary', p_summary, p_exec)
                logger.info("PyPdf Summary completed")
                st.download_button(
                    label="Download PyPDF Extracted Data",
                    data=pypdf_text,
                    file_name="pypdf_extraction.txt"
                )
                st.download_button(
                    label="Download PyPDF Summary",
                    data=generate_summary_text(p_summary, p_exec),
                    file_name="pypdf_summary.txt"
                )
            os.remove(file_name)
            logger.info("File removed")
except:
    st.error("Something went wrong!")
    st.error("Please check the PDF link and try again!")
    logger.info("Watch out! Something happened!")
    os.remove(file_name)







