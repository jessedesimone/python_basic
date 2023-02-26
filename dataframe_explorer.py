#!/usr/bin/env python3

'''basic dataframe exploration code'''

# import packages
import os
import pandas as pd
import xlsxwriter

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

'''
# get column names
#print(df.columns)

# fix some column headers
df = df.rename(columns={"A": "a",
                   "B": "b"})

# define covariates
covariates_list = ['<cov>', '<cov>']

# export covariates as csv
df2=df[covariates_list]
filepath=directories.data_dir + "covariates.csv"
df2.to_csv(filepath, index=False)

# standardize covariates and export as csv
import pandas as pd    
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
df2_scaled = pd.DataFrame(ss.fit_transform(df2),columns = df2.columns)
filepath=directories.data_dir + "covariates_ss.csv"
df2_scaled.to_csv(filepath, index=False)

'''