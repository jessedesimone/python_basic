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
import pandas as pd
pd.set_option('display.max_columns', None)
infile_name=input('Enter path/to/infile.xlsx\n> ');
def excel_reader(infile):
    df = pd.read_excel(
        io=infile,
        engine="openpyxl",
        #sheet_name=sheet,
        #nrows=1000
    )
    return df
df = excel_reader(infile_name)
print(df.info())


