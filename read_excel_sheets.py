'''Module to read separate sheets in excel file'''
pd.set_option('display.max_columns', None)
file1, file2 = None, None
with pd.ExcelFile(<path/to/file> + '<infile>') as reader:
    file1 = pd.read_excel(reader, sheet_name='<sheet name>')
    file2 = pd.read_excel(reader, sheet_name='<sheet name>')
