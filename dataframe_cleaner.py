#!/usr/bin/env python3

'''basic dataframe exploration code'''

# import packages
import os
import pandas as pd
import xlsxwriter
import numpy as np

# configure directories
class directories:
    '''Should be accessible in each module'''
    base_dir = '<infile>' 
    data_dir = os.path.join(base_dir, '<additional path>/')

# define infile
infile='<infile>'

# read file
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#file1, file2 = None, None
#with pd.ExcelFile(<path/to/file> + '<infile>') as reader:
    #file1 = pd.read_excel(reader, sheet_name='<sheet name>')
    #file2 = pd.read_excel(reader, sheet_name='<sheet name>')
df = pd.read_csv(directories.data_dir + infile)

print(df.info())
#print(df.describe())

nan_count = df.isna().sum()
print(nan_count)

# get column names
print(df.columns)

# rename column headers
df = df.rename(columns={"A": "a",
                   "B": "b"})

# create list
covariates_list = ['<cov>', '<cov>']

#drop columns conditional
df = df.drop(['subj', 'grp_id'], axis=1)

# drop rows conditional
df = df.dropna(subset=['FL_ALGRTHMC_DX'], axis=0)  
df = df.drop(df[df['FL_ALGRTHMC_DX'] == 9].index) 
df = df.drop(df[(df['COGSTATUS'] == 'dementia') & (df['DEMENTED'] == 0)].index)
# create conditional column
conditions = [
    (df['FL_ALGRTHMC_DX'] == 0),
    (df['FL_ALGRTHMC_DX'] == 2) | (df['FL_ALGRTHMC_DX'] == 3) | (df['FL_ALGRTHMC_DX'] == 22),
    (df['FL_ALGRTHMC_DX'] == 61) | (df['FL_ALGRTHMC_DX'] == 62),
    (df['FL_ALGRTHMC_DX'] == 5)
    ]
values = ['normal', 'mci', 'pre_mci', 'dementia']
df['COGSTATUS'] = np.select(conditions, values)

#move column position
# extract column 'COGSTATUS' from the DataFrame and insert at position 22
column_extract = df.pop('COGSTATUS')
df.insert(22, 'COGSTATUS', column_extract, allow_duplicates=True)

# conditional dataframe filtering
# subset columns
cols = ['<col>', '<col>']
df = df[cols]

# subset rows with string
# get rows with col value greater than 80    
df[df['<column>'].str.contains('<string>')]
df[df['<column>'].str.contains('<string>')]
df = df.loc[df['<column>'] > 80]                    

# multiple conditions
# get all rows with column value matching either string
options = ['<string1>', '<string2>']
df = df[df['<column>'].isin(options)]          

# get all rows matching multiple conditions
options = ['<string1>', '<string2>']
rslt_df = df[(df['<col1>'] == 21) & df['<col2>'].isin(options)]

#fill missing vals
#loop option
loop_cols = df.loc[:, df.columns!='grp']    #loop all cols except grouping variable
col_names = [col for col in loop_cols]
for col in col_names:
    df[col] = df[col].fillna(df.groupby('grp')[col].transform('median'))      #transform according to group median
