#!/usr/bin/env python3

'''
Module to read excel sheet and remove duplicates
Example below will keep the first instance of the defined column variable, so sort prior to running if needed

'''

#import packages
import os
import pandas as pd

#set directory and load file
file_path = '/Users/jessedesimone/Desktop'
os.chdir(file_path)

#load file 
infile='input.xlsx'
df=pd.read_excel(infile)

#set output
outfile='output.xlsx'

# Select the first instance of each unique subject ID
df_first_instance = df.drop_duplicates(subset='RID', keep='first')

# Save the resulting dataframe to a new Excel file (optional)
df_first_instance.to_excel(outfile, index=False)

print(df_first_instance)