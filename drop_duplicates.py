#!/usr/bin/env python3
'''
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
Return DataFrame with duplicate rows removed, optionally only considering certain columns

'''
import os
import pandas as pd

os.chdir('/Users/jessedesimone/Desktop')

df = pd.read_csv('infile.csv')
#df=df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
df=df.drop_duplicates(subset='PTID', keep='first', inplace=False, ignore_index=False)
df.to_csv('outfile.csv')
