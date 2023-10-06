# ...
from diagrams import Diagram

# ...

with Diagram("Architecture Diagram Part-1", show=False, direction='LR'):
    # Create a Cluster named "Source of Data"
    with Cluster("Source of Data"):
        online_file1 = SQL("SEC Public Form Pdf1")
        online_file2 = SQL("SEC Public Form Pdf2")

    pypdf_url = "https://github.com/Akshathapatil1998/Bigdata-Systems-Intelligent-Analytics/raw/main/pypdf1.jpeg"
    pypdf_icon = "pypdf.jpeg"
    urlretrieve(pypdf_url, pypdf_icon)

    nougat_url = "https://github.com/Akshathapatil1998/Bigdata-Systems-Intelligent-Analytics/raw/main/nougat.jpeg"
    nougat_icon = "nougat.jpeg"
    urlretrieve(nougat_url, nougat_icon)


    spacy_url="https://github.com/Akshathapatil1998/Bigdata-Systems-Intelligent-Analytics/raw/main/spacy.jpeg"
    spacy_icon = "spacy.jpeg"
    urlretrieve(spacy_url, spacy_icon)

    # Create a custom component for Streamlit
    streamlit = Custom("streamlit", streamlit_icon)

    # Create a custom component for Nougat
    nougat = Custom("Nougat", nougat_icon)

    pypdf=Custom("PyPdf",pypdf_icon)

    spacy=Custom("Spacy",spacy_icon)

    # CloudWatch = Cloudwatch('Amazon Cloud Watch')

    # Connect the data sources directly to the Python component
    online_file1 >> streamlit
    online_file2 >> streamlit

    # Connect the Python component to the Streamlit component
    streamlit >> nougat
    streamlit >> pypdf

    nougat >> spacy
    pypdf >> spacy

    

# Render the diagram (if "show=False" is removed, the diagram will be displayed)
# data_extraction.render()
