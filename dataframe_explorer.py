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

#drop columns
df = df.drop(['subj', 'grp_id'], axis=1)

# conditional dataframe filtering
# subset columns
cols = ['<col>', '<col>']
df = df[cols]

# subset rows with string
# get rows with col value greater than 80    
df[df.['<column>'].str.contains('<string>')]
df[df.['<column>'].str.contains('<string>')]
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

# get group means and sem
'''aggregate mean and sem into single dataframe'''
df_agg = pd.DataFrame(df.groupby('grp').agg(['mean','sem']))
df_agg=df_agg.reset_index()
df_agg.to_csv('means_sem.csv', index=False)