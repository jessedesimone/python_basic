#!/usr/bin/env python3

'''
module to merge xlsx sheets using pandas
out new dataframe as xlsx

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

#make columns to match same Dtype
file2.PTID.astype('int64')

df_merge = pd.merge(
    left=file1,
    right=file2,
    left_on="<column name>",
    right_on="<column name>",
    how="inner"
)

#output to excel sheet
df_merge.to_excel('<output name>.xlsx')
