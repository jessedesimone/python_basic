#!/usr/bin/env python3
'''
Module for subsetting dataframe based on list from another dataframe

'''
import os
import pandas as pd

#set wd
os.chdir('/Users/jessedesimone/Desktop') 

#source list
#read csv and covert to list
df_list=pd.read_csv('roi_list.csv')
var_list=df_list['variables'].tolist()

#optionally create list here
#var_list=['A', 'B', 'C', ... 'D']

#read df to subset
df=pd.read_csv('fw_data.csv')
df2=df[var_list]

df2.to_csv('df_subset.csv', index=False)
