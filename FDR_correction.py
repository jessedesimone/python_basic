#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:49:33 2019

@author: jessedesimone

This is an automated script to run FDR correction on a single column of p-values located in 
an excel spreadsheet; creates list of new p-values (newvals)

Spreadsheet should be saved to working directory defined below

Spreadsheet format
pvals (header)
p
p
p
p
...

Two options

"""


#%%
#import packages
import os
import pandas as pd
import numpy as np
import statsmodels.stats.multitest as multi

#%%
os.chdir('/Users/jessedesimone/Desktop')    #set working directory

#%%
df=pd.read_excel('Book16.xlsx')

#%%
pvals=df['pvals'].tolist()

#%%
# Option 1
multi.multipletests(pvals, alpha=0.05, method='fdr_bh', 
                                        is_sorted=False, returnsorted=False)

#%%
# Option 2

#define FDR correction function
def p_adjust_bh(p):
    """Benjamini-Hochberg p-value correction for multiple hypothesis testing."""
    p = np.asfarray(p)
    by_descend = p.argsort()[::-1]
    by_orig = by_descend.argsort()
    steps = float(len(p)) / np.arange(len(p), 0, -1)
    q = np.minimum(1, np.minimum.accumulate(steps * p[by_descend]))
    return q[by_orig]

newvals=p_adjust_bh(pvals)    #submit list of p-values for correction
newvals.tolist()      #convert array to list

