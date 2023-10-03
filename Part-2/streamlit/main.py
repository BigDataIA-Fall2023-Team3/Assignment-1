
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from io import BytesIO
import tempfile
import shutil

def generate_summary(file_content, file_name):
    if file_content is not None:
        try:
            # Try decoding with UTF-8st
            df = pd.read_excel(BytesIO(file_content))
        except Exception as e:
            st.write(f"Failed to read the file: {e}")
            return

        profile = ProfileReport(df, title=f"Summary for {file_name}", explorative=True)
        # Generate the HTML content of the profiling report
        profile_html = profile.to_html()

        # Display the HTML content within Streamlit using st.components.v1.html
        st.components.v1.html(profile_html, height=800, width=1000)

        # Save the HTML content to a temporary file
        temp_dir = tempfile.mkdtemp()
        temp_file_path = f"{temp_dir}/{file_name}_summary.html"
        with open(temp_file_path, "w", encoding="utf-8") as temp_file:
            temp_file.write(profile_html)

        # Provide an option to download the summary report
        st.download_button(
            label=f"Download {file_name} Summary",
            data=open(temp_file_path, "rb").read(),
            file_name=f"{file_name}_summary.html",
            key=file_name,
        )

        # Clean up temporary files
        shutil.rmtree(temp_dir)
    else:
        st.write(f"Failed to upload the {file_name} file. Please check the file.")

# Create a file uploader for both origination and monthly performance files
uploaded_files = st.file_uploader("Upload Excel Files (Origination and Monthly Performance)", type=["xls", "xlsx"], accept_multiple_files=True)

# Button to trigger the summary generation for each uploaded file
if st.button("Generate Summary") and uploaded_files:
    for file in uploaded_files:
        st.write(f"Generating summary for {file.name}...")
        file_name = file.name
        file_content = file.read()
        generate_summary(file_content, file_name)


