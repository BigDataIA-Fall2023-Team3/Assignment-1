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
    # If there's a file uploaded, then process it.
    validator = context.sources.pandas_default.read_csv(file_path)
    validator.expect_column_values_to_not_be_null("Loan Sequence Number")
    validator.expect_column_values_to_be_of_type("Loan Sequence Number","str")
    validator.expect_column_values_to_match_regex("Loan Sequence Number", regex=r'^[FA](?:[0-9]{2}[1-4]|[0-9]{2}[5-9][0-9])[0-9]{7}$')


    #Monthly Reporting Period
    validator.expect_column_values_to_not_be_null("Monthly Reporting Period")
    validator.expect_column_values_to_match_regex("Monthly Reporting Period",r"\d+")
    validator.expect_column_value_lengths_to_be_between("Monthly Reporting Period",1,6)

    #Current Actual UPB
    validator.expect_column_values_to_be_of_type('Current Actual UPB', type_='float')
    validator.expect_column_values_to_be_in_set('Current Actual UPB',value_set= ['XX', '0', '1', '2', '3', 'RA'] )

    #Loan Age
    validator.expect_column_values_to_be_of_type("Loan Age","int")
    validator.expect_column_value_lengths_to_be_between("Loan Age",1,3)

    #Remaining Months to Legal Maturity
    validator.expect_column_values_to_be_of_type("Remaining Months to Legal Maturity","int")
    validator.expect_column_value_lengths_to_be_between("Remaining Months to Legal Maturity",1,3)

    #Defect Settlement Date
    validator.expect_column_values_to_not_be_null("Defect Settlement Date")
    validator.expect_column_values_to_match_regex("Defect Settlement Date",r"\d+")
    validator.expect_column_value_lengths_to_be_between("Defect Settlement Date",1,6)

    #Modification Flag
    validator.expect_column_values_to_be_of_type("Modification Flag","str")
    validator.expect_column_values_to_be_in_set("Modification Flag",value_set=['Y', 'P'])

    #Zero Balance Code
    validator.expect_column_values_to_be_of_type("Zero Balance Code","int")
    validator.expect_column_value_lengths_to_be_between("Zero Balance Code",1,2)
    validator.expect_column_values_to_be_in_set(column='Zero Balance Code', value_set=['01', '02', '03', '96', '09', '15', '16'], mostly=1.0)

    #Zero Balance Effective Date
    validator.expect_column_values_to_match_regex("Zero Balance Effective Date",r"\d+")
    validator.expect_column_value_lengths_to_be_between("Zero Balance Effective Date",1,6)

    #Current Interest Rate
    validator.expect_column_values_to_be_of_type("Current Interest Rate","float")

    #Current Deferred UPB
    validator.expect_column_values_to_be_of_type("Current Deferred UPB","int")

    #Due Date of Last Paid Installment (DDLPI)
    validator.expect_column_values_to_match_regex("Due Date of Last Paid Installment (DDLPI)",r"\d+")
    validator.expect_column_value_lengths_to_be_between("Due Date of Last Paid Installment (DDLPI)",1,6)

    #MI Recoveries
    validator.expect_column_values_to_be_of_type("MI Recoveries","float")

    #Net Sales Proceeds
    validator.expect_column_values_to_be_of_type("Net Sales Proceeds","float")

    #Non MI Recoveries
    validator.expect_column_values_to_be_of_type("Non MI Recoveries","float")

    #Expenses
    validator.expect_column_values_to_be_of_type("Expenses","float")

    #Legal Costs
    validator.expect_column_values_to_be_of_type("Legal Costs","float")

    #Legal Costs
    validator.expect_column_values_to_be_of_type("Expenses","float")

    #Maintenance and Preservation Costs
    validator.expect_column_values_to_be_of_type("Maintenance and Preservation Costs","float")

    #Taxes and Insurance
    validator.expect_column_values_to_be_of_type("Taxes and Insurance","float")

    #Miscellaneous Expenses
    validator.expect_column_values_to_be_of_type("Miscellaneous Expenses","float")

    #Actual Loss Calculation
    validator.expect_column_values_to_be_of_type("Actual Loss Calculation","float")

    #Modification Cost
    validator.expect_column_values_to_be_of_type("Modification Cost","float")

    #Step Modification Flag
    validator.expect_column_values_to_be_in_set("Step Modification Flag",value_set=['Y', 'N'] )
    validator.expect_column_values_to_be_in_set("Step Modification Flag",value_set=['Space (1)'] )

    #Deferred Payment Plan
    validator.expect_column_values_to_be_in_set("Deferred Payment Plan",value_set=['Y', 'P'] )
    validator.expect_column_values_to_be_in_set("Deferred Payment Plan",value_set=['Space (1)'] )

    #Estimated Loan-to-Value (ELTV)
    validator.expect_column_values_to_be_between("Estimated Loan-to-Value (ELTV)",min_value=1,max_value=998)
    validator.expect_column_values_to_be_in_set("Estimated Loan-to-Value (ELTV)",value_set=['999', ''] )

    #Zero Balance Removal UPB
    validator.expect_column_values_to_be_of_type("Zero Balance Removal UPB","float")

    #Delinquent Accrued Interest
    validator.expect_column_values_to_be_of_type("Delinquent Accrued Interest","float")

    #Delinquency Due to Disaster
    validator.expect_column_values_to_be_in_set("Deferred Payment Plan",value_set=['Y'] )

    #Borrower Assistance Status Code
    validator.expect_column_values_to_be_in_set("Borrower Assistance Status Code",value_set=['F', 'R', 'T'] )

    #Current Month Modification Cost
    validator.expect_column_values_to_be_of_type("Current Month Modification Cost","float")

    #Interest Bearing UPB
    validator.expect_column_values_to_be_of_type("Interest Bearing UPB","float")


    validator.save_expectation_suite()


    checkpoint = context.add_or_update_checkpoint(
        name="my_quickstart_checkpoint",
        validator=validator,
    )

    checkpoint_result = checkpoint.run()

    # Assuming your current working directory is already set to "./gx/results"
    context.build_data_docs()

    directory = "./gx/results/"  # Replace with the path to your folder
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

else:
    st.warning("Please upload a CSV file.")

   