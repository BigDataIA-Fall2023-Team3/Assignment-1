import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from io import BytesIO
import tempfile
import shutil


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



