import great_expectations as gx
import pandas as pd
import streamlit as st 
import os

import zipfile
import io

def zipdir(path, ziph):
    # Zip the directory and all its contents, including sub-folders
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, path)
            ziph.write(file_path, arcname)

def create_zip(directory_to_zip):
    # Create a zip file in memory from the given directory
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        zipdir(directory_to_zip, zf)
    return memory_file


context = gx.get_context()

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])

analyze_button = st.button("Analyze")

if upload_file and analyze_button:

    file_path = os.path.join(upload_file.name)

    # Save the temporary uploaded file to the constructed file path
    with open(file_path, "wb") as f:
        f.write(upload_file.getbuffer())

    validator = context.sources.pandas_default.read_csv(file_path)


    #Credit Score
    validator.expect_column_values_to_not_be_null("Credit Score")
    validator.expect_column_values_to_be_of_type("Credit Score","int")
    validator.expect_table_row_count_to_be_between(min_value=300, max_value=850, include_in_result=True)

    #First Payment Date
    validator.expect_column_values_to_not_be_null("First Payment Date")
    # validator.expect_column_values_to_be_between("First Payment Date",202201,202212)
    validator.expect_column_values_to_match_regex("First Payment Date", r"^\d{6}")

    #First Time Homebuyer Flag
    validator.expect_column_values_to_not_be_null("First Time Homebuyer Flag")
    validator.expect_column_values_to_match_regex("First Time Homebuyer Flag",r"^[a-zA-Z0-9]+$")
    validator.expect_column_values_to_be_in_set("First Time Homebuyer Flag",['Y','N'])
    validator.expect_column_values_to_be_in_set("First Time Homebuyer Flag",['9'],  mostly = 0.1)



    #Maturity Date
    validator.expect_column_values_to_not_be_null("Maturity Date")
    validator.expect_column_values_to_match_regex("First Time Homebuyer Flag",r"\d+")
    validator.expect_column_value_lengths_to_be_between("Maturity Date",1,6)

    #Metropolitan Statistical Area (MSA) Or Metropolitan Division
    validator.expect_column_values_to_be_in_set("Metropolitan Statistical Area (MSA) Or Metropolitan Division", value_set=['Space (5)'], mostly=1.0)
    validator.expect_column_values_to_be_of_type("Metropolitan Statistical Area (MSA) Or Metropolitan Division","int")
    validator.expect_column_value_lengths_to_be_between("Metropolitan Statistical Area (MSA) Or Metropolitan Division",1,5)

    #Mortgage Insurance Percentage (MI %)
    validator.expect_column_values_to_not_be_null("Mortgage Insurance Percentage (MI %)")
    validator.expect_column_values_to_be_of_type("Mortgage Insurance Percentage (MI %)","int")
    validator.expect_column_value_lengths_to_be_between("Mortgage Insurance Percentage (MI %)",1,3)
    validator.expect_column_values_to_be_between( "Mortgage Insurance Percentage (MI %)", min_value=1, max_value=55,  mostly=0.8)
    validator.expect_column_values_to_be_in_set("Mortgage Insurance Percentage (MI %)",value_set=['0', '999'], mostly=0.0)

    #Number of Units
    validator.expect_column_values_to_not_be_null("Number of Units")
    validator.expect_column_values_to_be_of_type("Number of Units","int")
    validator.expect_column_value_lengths_to_be_between("Number of Units",1,2)
    validator.expect_column_values_to_be_in_set("Number of Units",value_set=['1', '2', '3', '4'], mostly=1.0)

    #Occupancy Status
    validator.expect_column_values_to_not_be_null("Occupancy Status")
    validator.expect_column_values_to_be_of_type("Occupancy Status","str")
    validator.expect_column_values_to_be_in_set("Occupancy Status",value_set=['P', 'I', 'S'], mostly=1.0)
        

    #Original Combined Loan-to-Value (CLTV)
    validator.expect_column_values_to_not_be_null("Original Combined Loan-to-Value (CLTV)")
    validator.expect_column_values_to_be_of_type("Original Combined Loan-to-Value (CLTV)","int")
    validator.expect_column_value_lengths_to_be_between("Original Combined Loan-to-Value (CLTV)",1,3)

    #Original Debt-to-Income (DTI) Ratio
    validator.expect_column_values_to_be_of_type("Original Debt-to-Income (DTI) Ratio","int")
    validator.expect_column_value_lengths_to_be_between("Original Debt-to-Income (DTI) Ratio",1,3)
    validator.expect_column_values_to_be_between( "Original Debt-to-Income (DTI) Ratio", min_value=0, max_value=65,  mostly=1.0)


    #Original UPB
    validator.expect_column_values_to_be_of_type("Original UPB","int")
    validator.expect_column_value_lengths_to_be_between("Original UPB",1,12)

    #Original Loan-to-Value (LTV)
    validator.expect_column_values_to_be_of_type("Original Loan-to-Value (LTV)","int")
    validator.expect_column_value_lengths_to_be_between("Original Loan-to-Value (LTV)",1,3)

    #Original Interest Rate
    validator.expect_column_values_to_be_of_type("Original Interest Rate","float")

    #Channel
    validator.expect_column_values_to_be_of_type("Channel","str")
    validator.expect_column_values_to_be_in_set("Channel",value_set=['R', 'B', 'C', 'T'],mostly=1.0)

    #Prepayment Penalty Mortgage (PPM) Flag
    validator.expect_column_values_to_be_of_type("Prepayment Penalty Mortgage (PPM) Flag","str")
    validator.expect_column_values_to_be_in_set("Prepayment Penalty Mortgage (PPM) Flag",value_set=['Y', 'N'],mostly=1.0)


    #Amortization Type (Formerly Product Type)
    validator.expect_column_values_to_be_of_type("Amortization Type (Formerly Product Type)","str")
    validator.expect_column_values_to_be_in_set("Amortization Type (Formerly Product Type)",value_set=['FRM', 'ARM'],mostly=1.0)


    #Property State
    validator.expect_column_values_to_be_of_type("Property Type","str")
    validator.expect_column_values_to_be_in_set("Property Type", value_set=['CO', 'PU', 'MH', 'SF', 'CP'])

    #Property Type
    states = [
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY',
    ]

    # Add all valid state abbreviations
    validator.expect_column_values_to_be_of_type("Property State","str")
    validator.expect_column_values_to_match_regex("Property State",regex=r'^[A-Z]{2}$', mostly=1.0)
    validator.expect_column_values_to_be_in_set("Property State",value_set=states, mostly=1.0) 

    #Postal Code
    validator.expect_column_values_to_be_of_type("Postal Code","int")
    validator.expect_column_values_to_match_regex("Postal Code", regex=r'^\d{3}00$')
    validator.expect_column_values_to_be_in_set("Postal Code",value_set=['Space (5)'], mostly=0.0)

    #Loan Sequence Number
    validator.expect_column_values_to_be_of_type("Loan Sequence Number","str")
    validator.expect_column_values_to_match_regex("Loan Sequence Number", regex=r'^[FA](?:[0-9]{2}[1-4]|[0-9]{2}[5-9][0-9])[0-9]{7}$')


    #Loan Purpose
    validator.expect_column_values_to_be_of_type("Loan Purpose","str")
    validator.expect_column_values_to_be_in_set("Loan Purpose",value_set=['P', 'C', 'N', 'R'] ,mostly=1.0)

    #Original Loan Term
    validator.expect_column_values_to_be_of_type("Original Loan Term","int")
    validator.expect_column_value_lengths_to_be_between("Original Loan Term",1,3)


    #Number of Borrowers
    validator.expect_column_values_to_be_of_type("Number of Borrowers","int")

    #Seller Name
    validator.expect_column_values_to_be_of_type("Seller Name","str")
    validator.expect_column_value_lengths_to_be_between("Seller Name",1,60)


    #Servicer Name
    validator.expect_column_values_to_be_of_type("Servicer Name","str")
    validator.expect_column_value_lengths_to_be_between("Servicer Name",1,60)


    #Super Conforming Flag
    validator.expect_column_values_to_be_of_type("Super Conforming Flag","str")
    validator.expect_column_values_to_be_in_set("Super Conforming Flag",value_set=['Y'])

    #Pre-HARP Loan Sequence Number
    validator.expect_column_values_to_be_of_type("Pre-HARP Loan Sequence Number","str")
    validator.expect_column_values_to_match_regex("Pre-HARP Loan Sequence Number", regex=r'^[FA](?:[0-9]{2}[1-4]|[0-9]{2}[5-9][0-9])[0-9]{7}$')


    #Program Indicator
    validator.expect_column_values_to_be_of_type("Program Indicator","str")
    validator.expect_column_values_to_be_in_set("Program Indicator",value_set=['H', 'F', 'R'] )

    #HARP Indicator
    validator.expect_column_values_to_be_of_type("HARP Indicator","str")
    validator.expect_column_values_to_be_in_set("HARP Indicator",value_set=['Y'] )


    #Property Valuation Method
    validator.expect_column_values_to_be_of_type("Property Valuation Method","int")
    validator.expect_column_values_to_be_in_set("Property Valuation Method",value_set=['1', '2', '3', '4'] )


    #Interest Only (I/O) Indicator
    validator.expect_column_values_to_be_of_type("Interest Only (I/O) Indicator","str")
    validator.expect_column_values_to_be_in_set("Interest Only (I/O) Indicator",value_set=['Y', 'N'] )


    #Mortgage Insurance Cancellation Indicator
    validator.expect_column_values_to_be_of_type("Mortgage Insurance Cancellation Indicator","str")
    validator.expect_column_values_to_be_in_set("Mortgage Insurance Cancellation Indicator",value_set=['Y', 'N'] )



    validator.save_expectation_suite()

    checkpoint = context.add_or_update_checkpoint(
        name="my_quickstart_checkpoint",
        validator=validator,
    )

    checkpoint_result = checkpoint.run()
    context.build_data_docs()

    directory = "/app/assignment-1/Part-2/streamlit/gx/results/"  # Replace with the path to your folder
    zip_filename = "Download.zip"

    zip_filename = "folder_content.zip"
    # contents = os.listdir(directory)

    # for item in contents:
    #     st.write(item)

    st.write("Click the button below to download the folder as a ZIP file:")
    file = create_zip(directory)
    st.download_button(
            label="Download",
            data=file,
            file_name="Files.zip",
            mime="application/zip"
            )
    os.remove(file_path)

    

    # st.write(checkpoint_result)
else:
    st.write("### Please upload a file to run the check")



