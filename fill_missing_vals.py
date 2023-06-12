#!/usr/bin/env python3

#module to fill missing values with mean or median

#import packages
import pandas as pd

df = pd.read_csv('/path/to/csv')
df_c=df #make copy of df
df_c['<column name>'] = df_c['<column name>'].fillna(df_c.groupby('<grouping variable>')['column name'].transform('median'))
df_c['<column name>'] = df_c['<column name>'].fillna(df_c.groupby('<grouping variable>')['column name'].transform('mean'))

