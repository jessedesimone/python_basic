#!/usr/bin/env python3
"""
Copyright (C) 2021 Jesse DeSimone, Ph.D.

Change Log
=============
Version 1.0.0
-------------
First Release

Use:
-input number of uncorrected p-values to correct for as <int>
-input uncorrected p-values as <float>

Output
Table with uncorrected and corrected p-values
FDR_out.csv

"""
# PACKAGES
import numpy as np
import pandas as pd

list_of_p = []
# RUNNER
def number_req():
    num_of_in = int(input('Enter <int> number of uncorrected p-values: '))
    while True:
        if len(list_of_p) == num_of_in:
            break
        else:
            unc_p = float(input('Enter <float> uncorrected p-value: '))
            list_of_p.append(unc_p)

number_req()

#define FDR correction function
def p_adjust_bh(p):
    """Benjamini-Hochberg p-value correction for multiple hypothesis testing."""
    p = np.asfarray(p)
    by_descend = p.argsort()[::-1]
    by_orig = by_descend.argsort()
    steps = float(len(p)) / np.arange(len(p), 0, -1)
    q = np.minimum(1, np.minimum.accumulate(steps * p[by_descend]))
    return q[by_orig]

newvals = p_adjust_bh(list_of_p)    #submit list of p-values for correction
newvals.tolist()      #convert array to list

# CREATE DATAFRAME
d = {'Uncorrected':list_of_p, 'FDR':newvals}
df = pd.DataFrame(d)
print(df)
df.to_csv('test.csv')

