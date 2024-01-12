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



## -------------- option 2 --------------
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
