#!/usr/bin/env python3
'''
Module for reading csv data file and converting to dataframe

'''
import os
import pandas as pd
pd.set_option('display.max_columns', None)

def file_path():
    fpath = input('\nEnter <path/to/infiles>: ')
    print('\nPath to input files: ', fpath)
    print('\nFiles in Directory:')
    print(os.listdir(fpath))
    return(fpath)

def data_reader(fname):
    fh = os.path.join(path, fname)
    return pd.read_csv(fh)

if __name__ == '__main__':
    path = file_path()
    df = data_reader()
