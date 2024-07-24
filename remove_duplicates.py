#!/usr/bin/env python3

'''
Module to read excel sheet and remove duplicates
Example below will keep the first instance of the defined column variable, so sort prior to running if needed

'''
# Read the Excel file
file_path = '/Users/jessedesimone/Desktop/merged_date.xlsx'  # Replace with your actual file path
sheet_name = 'Sheet1'  # Replace with the actual sheet name

# Read the sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Check for duplicates based on SUBJ_ID, DATE_B, and DATE_F
duplicates = df[df.duplicated(subset=['SUBJ_ID', 'DATE_B', 'DATE_F'], keep=False)]

# Print duplicates if found
if not duplicates.empty:
    print("Duplicates found:")
    print(duplicates)

# Remove duplicates based on SUBJ_ID, DATE_B, and DATE_F, keeping the first occurrence
df_cleaned = df.drop_duplicates(subset=['SUBJ_ID', 'DATE_B', 'DATE_F'], keep='first')

# Display the cleaned DataFrame
print(df_cleaned)

# Optionally, save the cleaned DataFrame to a new Excel file
output_file_path = 'cleaned_data.xlsx'  # Replace with your desired output file path
df_cleaned.to_excel(output_file_path, index=False)