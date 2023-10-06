import pandas as pd
import logging
import streamlit as st
from pandas_profiling import ProfileReport
from io import BytesIO
import boto3



# AWS credentials
aws_access_key_id = st.secrets['AWS_ACCESS_KEY_ID']
aws_secret_access_key = st.secrets['AWS_SECRET_ACCESS_KEY']
aws_region = 'us-east-1'
# boto3.setup_default_session(region_name=aws_region)
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,region_name=aws_region)

formatter = logging.Formatter('%(asctime)s : %(levelname)s - %(message)s')


# S3 bucket name
s3_bucket_name = 'assignment-1-part-2' 




st.title("File Summary Generator")

def generate_summary(file_content, file_name):
   
    if file_content is not None:
        try:
            # Try decoding with UTF-8
            df = pd.read_csv(BytesIO(file_content))
        except Exception as e:
            st.write(f"Failed to read the file: {e}")
            return

        profile = ProfileReport(df, title=f"Summary for {file_name}", explorative=True)
        # Generate the HTML content of the profiling report
        profile_html = profile.to_html()

        # Display the HTML content within Streamlit using st.components.v1.html
        st.components.v1.html(profile_html, height=800, width=1000)
        s3_key = f"summary/{file_name}_profile.html" 
        s3_client.put_object(Bucket=s3_bucket_name, Key=s3_key, Body=profile_html.encode('utf-8'))



        html_file_exists = s3_client.head_object(Bucket=s3_bucket_name, Key=s3_key)

        if html_file_exists:
                # Generate a temporary download link
                s3_download_link = f"https://{s3_bucket_name}.s3.amazonaws.com/{s3_key}"

                # Display the download link
                st.write(f"Download your HTML profile report [here]({s3_download_link})")
        else:
            st.warning("HTML file not found in S3. Please upload it first.")

    else:
        st.write(f"Failed to upload the {file_name} file. Please check the file.")


# Create a dropdown to select which file to upload
selected_file = st.selectbox("Select File to Upload", ("Origination CSV", "Monthly Performance CSV"))




# File upload based on the selected option
if selected_file == "Origination CSV":

    uploaded_file = st.file_uploader("Upload Origination CSV File", type=["csv"])
elif selected_file == "Monthly Performance CSV":
    uploaded_file = st.file_uploader("Upload Monthly Performance CSV File", type=["csv"])
    

# Button to trigger the summary generation
if st.button("Generate Summary") and uploaded_file:
   
    st.write(f"Generating summary for {selected_file}...")
    file_name = uploaded_file.name
    file_content = uploaded_file.read()
    generate_summary(file_content, file_name)





