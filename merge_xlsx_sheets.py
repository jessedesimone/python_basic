#!/usr/bin/env python3

'''
module to merge xlsx sheets using pandas
out new dataframe as xlsx
before merging, good idea to make sure that Dtypes match for left_on and right_on column names

"how" options:
inner	selects records that have matching values in both dataframes.
left	returns all records from the left dataframe, and the matching records from the right dataframe. The result is null records from the right side, if there is no match.
right	returns all records from the right dataframe, and the matching records from the left dataframe. The result is null records from the left side, if there is no match.
outer	returns all records when there is a match in left or right dataframe records.
cross	returns cartesian product of both dataframes (number of rows in the first dataframe multiplied by the number of rows in the second dataframe).

'''

#import packages
import os
import pandas as pd

#set directory
os.chdir('/path/to/dir')

#excel reader
file1, file2 = None, None
with pd.ExcelFile('<file>.xlsx') as reader:
    file1 = pd.read_excel(reader, sheet_name='<sheet name>')
    file2 = pd.read_excel(reader, sheet_name='<sheet name>')

#fix dtypes
# DF=[file1, file2]
# for df in DF:
#     cols = df.columns[df.columns.str.contains('<string>')]  #find all columns containing specific string
#     df[cols] = df[cols].astype('<dtype>')        #change dtype for all cols

#set merge paramaters
left_file=file1
right_file=file2
left_header='<column header>'
right_header='<column header>'
how_type='<join type>'

#merge dataframes
df_merge = pd.merge(
    left=left_file,
    right=right_file,
    left_on=left_header,
    right_on=right_header,
    how=how_type
)

#output to excel sheet
df_merge.to_excel('df_merged_{}.xlsx'.format(how_type), index=False)


# Merging based on multiple columns
'''
# Read the Excel file
file_path = 'your_file.xlsx'  # Replace with your actual file path
sheet1_name = 'Sheet1'  # Replace with the actual sheet name
sheet2_name = 'Sheet2'  # Replace with the actual sheet name

# Read the two sheets into DataFrames
df1 = pd.read_excel(file_path, sheet_name=sheet1_name)
df2 = pd.read_excel(file_path, sheet_name=sheet2_name)

# Merge the DataFrames on SUBJ_ID and STUDY_DATE
merged_df = pd.merge(df1, df2, on=['COLUMN ID A', 'COLUMN ID B'], how='inner')

# Display the merged DataFrame
print(merged_df)

# Optionally, save the merged DataFrame to a new Excel file
output_file_path = 'merged_data.xlsx'  # Replace with your desired output file path
merged_df.to_excel(output_file_path, index=False)
'''