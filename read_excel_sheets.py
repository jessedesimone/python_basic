'''Module to read separate sheets in excel file'''

#------option 1 | manual entry-----
import pandas as pd
pd.set_option('display.max_columns', None)
file1, file2 = None, None
with pd.ExcelFile(<path/to/file> + '<infile>') as reader:
    file1 = pd.read_excel(reader, sheet_name='<sheet name>')
    file2 = pd.read_excel(reader, sheet_name='<sheet name>')


#------option 2-----
'''function to read single sheet'''
#import packages
import pandas as pd
import sys

#def infile
infile_name=input('Enter path/to/infile.xlsx\n> ');

#def class os error
class FileError(Exception):
    def __init__(self, filename):
        self.filename = filename
        
    def __str__(self):
        return f"++ Error in accessing file: {self.filename}\n ++ Check path"

#def excel reader function
def excel_reader(infile):
    df = pd.read_excel(
        io=infile,
        engine="openpyxl",
        #sheet_name=sheet,
        #nrows=1000
    )
    return df

print('++ reading data')
try:
    df = excel_reader(infile_name)
    print(df.info())
except:
    print(FileError(infile_name)); sys.exit()




