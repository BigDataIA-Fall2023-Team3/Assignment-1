## Assignment-1
# Financial Data Quality Assessment and Summarization Tool for SEC PDFs and Freddie Mac Datasets

### Project Description:
This project involves building a Streamlit-based tool that serves two primary purposes:

## Part 1: PDF Analyzer

- Allows users to input a link to a PDF document from the SEC website.
- Provides the option to choose between the "nougat" and "pypdf" libraries for PDF processing.
- The two data sources (PDF files) are connected directly to the "streamlit" component.
- From "streamlit," the data flows to two different custom components: "Nougat" and "PyPdf."
- Both "Nougat" and "PyPdf" components feed their processed data to a custom component called "Spacy." 

## Part 2: Data Quality Evaluation Tool 

- Data from the "Freddie Mac Origination File" and "Freddi Mac Monthly Performance File" is directed to the "Pandas Profiling" component for data processing.
- Enables users to upload CSV/XLS files containing either Origination or Monthly performance data from the Freddie Mac Single Family Dataset.
- Utilizes Pandas Profiling to generate data summaries and displays them to the end user.
- Executes Great Expectations tests to ensure the following:
- It goes to "Great Expectations (GX)," indicating that some kind of data validation or testing is performed.
- Data is stored in Amazon S3 for storage purposes and is monitored and tracked using "Amazon Cloud Watch.

## Architecture

### PDF Analyzer

![architecture_diagram_part-1](https://github.com/BigDataIA-Fall2023-Team3/Assignment-1/assets/71171604/e8a09a22-6a24-4efb-8a4f-89387330bde3)


### Data Quality Evaluation Tool 


![architecture_diagram-part2](https://github.com/BigDataIA-Fall2023-Team3/Assignment-1/assets/71171604/1ca233e5-f688-4010-80aa-b0e72727ddd1)



# File Structure


# Running the project

#### Create Virtual Environment

`python3 -m venv venv`

#### Installing Requirements 

`pip3 install -r requirements.txt`     #available in the root directory of the project

#### Running Streamlit App

- ` Streamlit run Main.py`               #Part 1
- ` Streamlit run Summary_Generator.py`   #Part2

WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT

AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

 ### Contribution: 


● Sumanayana Konda: 25% 

● Akshatha Patil: 25% 

● Ruthwik Bommenahalli Gowda: 25% 

● Pavan Madhav Manikantha Sai Nainala: 25% 

















