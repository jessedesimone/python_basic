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
roi_list=df_list['roi'].tolist()

#read df to subset
df=pd.read_csv('fw_data.csv')
df2=df[roi_list]

df2.to_csv('df_subset.csv', index=False)
