#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (C) Jesse DeSimone, Ph.D.
Created on Tue Aug  4 11:34:45 2020

"""
#%%
import os
#ROOT_DIR
PROJECT_ROOT_DIR = '/Users/jessedesimone/Desktop/HLE_test'

#SUB_DIR
DATA_PATH = os.path.join(PROJECT_ROOT_DIR, "Tables")

#INFILE
infile = ''

#READ DATA
def load_data(path=DATA_PATH):
    csv_path = os.path.join(path, infile)
    return pd.read_csv(csv_path)
df = load_data()


