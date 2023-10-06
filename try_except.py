import sys
import pandas as pd

'''use try except to read input excel file, throw error if not found'''

infile='hello.xlsx'
print('++ reading data')
try:
    df = pd.read_excel(infile)
except Exception as e:
    #print(e)
    sys.exit(e)