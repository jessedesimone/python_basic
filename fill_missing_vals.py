#!/usr/bin/env python3

#module to fill missing values with mean or median

#import packages
import pandas as pd

df = pd.read_csv('/path/to/csv')
df_c=df #make copy of df

#loop option
loop_cols = df_c.loc[:, df_c.columns!='grp']    #loop all cols except grouping variable
col_names = [col for col in loop_cols]
for col in col_names:
    df_c[col] = df_c[col].fillna(df_c.groupby('grp')[col].transform('median'))      #transform according to group median

#single column option
df_c['<column name>'] = df_c['<column name>'].fillna(df_c.groupby('<grouping variable>')['column name'].transform('median'))
df_c['<column name>'] = df_c['<column name>'].fillna(df_c.groupby('<grouping variable>')['column name'].transform('mean'))

