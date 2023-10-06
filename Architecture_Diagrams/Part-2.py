from pickle import FRAME
# ...
from diagrams import Diagram

from diagrams.gcp.analytics import BigQuery, Dataflow
from diagrams.elastic.elasticsearch import SQL
from diagrams.programming.language import Python
from diagrams.custom import Custom
from urllib.request import urlretrieve

from diagrams.aws.storage import SimpleStorageServiceS3BucketWithObjects
from diagrams.aws.storage import SimpleStorageServiceS3, S3

from diagrams.aws.management import Cloudwatch


with Diagram("Architecture Diagram Part-2", show=False):
    # Create a Cluster named "Source of Data"
    with Cluster("Source of Data"):
        origination_file = SQL("Freddie Mac Origination File")
        monthly_performance_file = SQL("Freddi Mac Monthly Performance File")

    # Create a component for the pandas profiling
    extraction = Python("Pandas Profiling")

    streamlit_url = "https://github.com/Akshathapatil1998/Bigdata-Systems-Intelligent-Analytics/raw/main/streamlit.jpeg"
    streamlit_icon = "streamlit.jpeg"
    urlretrieve(streamlit_url, streamlit_icon)

    gx_url = "https://github.com/Akshathapatil1998/Bigdata-Systems-Intelligent-Analytics/raw/main/gx.jpeg"
    gx_icon = "gx.jpeg"
    urlretrieve(gx_url, gx_icon)

    # Create a custom component for Streamlit
    streamlit = Custom("streamlit", streamlit_icon)

    # Create a custom component for GX
    gx= Custom("Great_Expectations", gx_icon)

    # Create a component for s3
    AmazonS3=S3('Amazons3')

    CloudWatch=Cloudwatch('Amazon Cloud Watch')
    # Connect the data sources directly to the Python component
    origination_file >> extraction
    monthly_performance_file >> extraction

    # Connect the Python component to the Streamlit component
    extraction >> streamlit

    # Connect the Streamlit component to the data loading process
    streamlit >> gx
    streamlit >> AmazonS3
    streamlit >> CloudWatch




# Render the diagram (if "show=False" is removed, the diagram will be displayed)
# data_extraction.render()

