
import great_expectations as gx
import pandas as pd
import streamlit as st 


print("line 7")
context = gx.get_context()
print("validator: on line 9")
validator = context.sources.pandas_default.read_excel(
    "/Users/keerthi/Desktop/sample_2022/Sample_orig_2022.xls"
)
print("validator:")
print(type(validator))
validator.expect_column_values_to_not_be_null("Credit Score")
validator.expect_column_values_to_be_of_type("Credit Score","int")
validator.expect_column_value_lengths_to_be_between("Credit Score",1,4)
# validator.expect_column_values_to_be_between("First Payment Date",202201,202212)

validator.expect_column_values_to_match_regex("First Payment Date", r"^\d{6}")

validator.save_expectation_suite()

checkpoint = context.add_or_update_checkpoint(
    name="my_quickstart_checkpoint",
    validator=validator,
)



checkpoint_result = checkpoint.run()

context.view_validation_result(checkpoint_result)

st.write(f"### Great Expectations Check Results ")
st.write(checkpoint_result)
