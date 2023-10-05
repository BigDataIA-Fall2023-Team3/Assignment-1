
import great_expectations as gx
import pandas as pd
import streamlit as st 


print("line 7")
context = gx.get_context()
print("validator: on line 9")

validator = context.sources.pandas_default.read_excel(
    "/Users/pavanmadhavnainala/Desktop/Big Data/Sample_orig_2022.xls"
   
)
# validator = context.sources.pandas_default.read_csv(
#      "/Users/keerthi/Desktop/sample_2022/Sample_orig_2022.csv"
    
# )

print("validator:")
print(type(validator))

#Credit Score
validator.expect_column_values_to_not_be_null("Credit Score")
validator.expect_column_values_to_be_of_type("Credit Score","int")
validator.expect_column_value_lengths_to_be_between("Credit Score",1,4)

#First Payment Date
validator.expect_column_values_to_not_be_null("First Payment Date")
# validator.expect_column_values_to_be_between("First Payment Date",202201,202212)
validator.expect_column_values_to_match_regex("First Payment Date", r"^\d{6}")

#First Time Homebuyer Flag
validator.expect_column_values_to_not_be_null("First Time Homebuyer Flag")
validator.expect_column_values_to_match_regex("First Time Homebuyer Flag",r"^[a-zA-Z0-9]+$")
validator.expect_column_values_to_be_in_set("First Time Homebuyer Flag",['Y','N'])


#Maturity Date
validator.expect_column_values_to_not_be_null("Maturity Date")
validator.expect_column_values_to_match_regex("First Time Homebuyer Flag",r"\d+")
validator.expect_column_value_lengths_to_be_between("Maturity Date",1,6)

#Metropolitan Statistical Area (MSA) Or Metropolitan Division
validator.expect_column_values_to_not_be_null("Metropolitan Statistical Area (MSA) Or Metropolitan Division")
validator.expect_column_values_to_be_of_type("Metropolitan Statistical Area (MSA) Or Metropolitan Division","int")
validator.expect_column_value_lengths_to_be_between("Metropolitan Statistical Area (MSA) Or Metropolitan Division",1,5)

#Mortgage Insurance Percentage (MI %)
validator.expect_column_values_to_not_be_null("Mortgage Insurance Percentage (MI %)")
validator.expect_column_values_to_be_of_type("Mortgage Insurance Percentage (MI %)","int")
validator.expect_column_value_lengths_to_be_between("Mortgage Insurance Percentage (MI %)",1,3)

#Number of Units
validator.expect_column_values_to_not_be_null("Number of Units")
validator.expect_column_values_to_be_of_type("Number of Units","int")
validator.expect_column_value_lengths_to_be_between("Number of Units",1,2)

#Occupancy Status
validator.expect_column_values_to_not_be_null("Occupancy Status")
validator.expect_column_values_to_be_of_type("Occupancy Status","str")

#Original Combined Loan-to-Value (CLTV)
validator.expect_column_values_to_not_be_null("Original Combined Loan-to-Value (CLTV)")
validator.expect_column_values_to_be_of_type("Original Combined Loan-to-Value (CLTV)","int")
validator.expect_column_value_lengths_to_be_between("Original Combined Loan-to-Value (CLTV)",1,3)

#Original Debt-to-Income (DTI) Ratio
validator.expect_column_values_to_be_of_type("Original Debt-to-Income (DTI) Ratio","int")
validator.expect_column_value_lengths_to_be_between("Original Debt-to-Income (DTI) Ratio",1,3)

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

#Prepayment Penalty Mortgage (PPM) Flag
validator.expect_column_values_to_be_of_type("Prepayment Penalty Mortgage (PPM) Flag","str")

#Amortization Type (Formerly Product Type)
validator.expect_column_values_to_be_of_type("Amortization Type (Formerly Product Type)","str")

#Property State
validator.expect_column_values_to_be_of_type("Property State","str")

#Property Type
validator.expect_column_values_to_be_of_type("Property Type","str")

#Postal Code
validator.expect_column_values_to_be_of_type("Postal Code","int")

#Loan Sequence Number
validator.expect_column_values_to_be_of_type("Loan Sequence Number","str")

#Loan Purpose
validator.expect_column_values_to_be_of_type("Loan Purpose","str")

#Original Loan Term
validator.expect_column_values_to_be_of_type("Original Loan Term","int")

#Number of Borrowers
validator.expect_column_values_to_be_of_type("Number of Borrowers","int")

#Seller Name
validator.expect_column_values_to_be_of_type("Seller Name","str")

#Servicer Name
validator.expect_column_values_to_be_of_type("Servicer Name","str")

#Super Conforming Flag
validator.expect_column_values_to_be_of_type("Super Conforming Flag","str")

#Pre-HARP Loan Sequence Number
validator.expect_column_values_to_be_of_type("Pre-HARP Loan Sequence Number","str")

#Program Indicator
validator.expect_column_values_to_be_of_type("Program Indicator","str")

#HARP Indicator
validator.expect_column_values_to_be_of_type("HARP Indicator","str")

#Property Valuation Method
validator.expect_column_values_to_be_of_type("Property Valuation Method","int")

#Interest Only (I/O) Indicator
validator.expect_column_values_to_be_of_type("Interest Only (I/O) Indicator","str")

#Mortgage Insurance Cancellation Indicator
validator.expect_column_values_to_be_of_type("Mortgage Insurance Cancellation Indicator","str")

validator.save_expectation_suite()

checkpoint = context.add_or_update_checkpoint(
    name="my_quickstart_checkpoint",
    validator=validator,
)



checkpoint_result = checkpoint.run()


context.view_validation_result(checkpoint_result)

st.write(f"### Great Expectations Check Results ")
st.write(checkpoint_result)
