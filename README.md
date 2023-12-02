## Assignment-1

#### [streamlit app Part-1](https://assignment-1-part-1.streamlit.app/)
#### [streamlit app Part-2](https://assignment-1-part-2.streamlit.app/)

#### [codelabs](https://codelabs-preview.appspot.com/?file_id=1i1HbF6HBoYjjqOs1vbqH3SOrUFYEOoYAvam3goFDWHM#0)

## Data Quality Assessment and Summarization Tool for SEC PDFs and Freddie Mac Datasets

### Project Description:
This project involves building a Streamlit-based tool that serves two primary purposes:

### Part 1: PDF Analyzer

- Allows users to input a link to a PDF document from the SEC website.
- Provides the option to choose between the "nougat" and "pypdf" libraries for PDF processing.
- The two data sources (PDF files) are connected directly to the "streamlit" component.
- From "streamlit," the data flows to two different custom components: "Nougat" and "PyPdf."
- Both "Nougat" and "PyPdf" components feed their processed data to a custom component called "Spacy." 

### Part 2: Data Quality Evaluation Tool 

- Data from the "Freddie Mac Origination File" and "Freddi Mac Monthly Performance File" is directed to the "Pandas Profiling" component for data processing.
- Enables users to upload CSV/XLS files containing either Origination or Monthly performance data from the Freddie Mac Single Family Dataset.
- Pandas Profiling is performed generate data summaries and displays them to the end user.
- Great Expectations tests are executed to ensure that the data adheres to the schema published by Freddie Mac by performing validations. This validation process ensures that the 
  data meets the specified criteria and quality standards.

### Technology Stack:
- Streamlit
- PyPdf
- Nougat
- Spacy
- Pandas Profiling
- Great Expectations
- AWS

### Architecture

#### PDF Analyzer
![WhatsApp Image 2023-10-05 at 10 37 38 PM](https://github.com/BigDataIA-Fall2023-Team3/Assignment-1/assets/114708712/0a00a911-9c1a-4a9e-883f-189c04612579)
#### Data Quality Evaluation Tool 
![architecture_diagram_part-2](https://github.com/BigDataIA-Fall2023-Team3/Assignment-1/assets/114708712/1bd788bb-420f-4e7d-859a-6c595d41badc)


### Navigation
Assignment-1

<img width="368" alt="Screen Shot 2023-10-06 at 6 07 23 PM" src="https://github.com/BigDataIA-Fall2023-Team3/Assignment-1/assets/114708712/d0aca0bb-d155-4933-a386-d29f15455796">

#### Create Virtual Environment

`python3 -m venv venv`

#### Installing Requirements 

`pip3 install -r requirements.txt`     #available in the root directory of the project

#### Running Streamlit App

- ` Streamlit run Main.py`               #Part 1
- ` Streamlit run Summary_Generator.py`   #Part2

WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT

AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

 ### Contributions: 

- Sumanayana Konda: 25% 
- Akshatha Patil: 25% 
- Ruthwik Bommenahalli Gowda: 25%
- Pavan Madhav Manikantha Sai Nainala: 25% 
















