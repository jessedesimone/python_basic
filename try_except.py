#import packages
import sys
import os
import pandas as pd

#define paths
top = '/Users/jessedesimone/desimone_github/ml/aidp'
data_dir = os.path.join(top + '/infiles')
os.chdir(data_dir)

#def class exception error
class NotValidPath(Exception):
  '''Raised when input file not found'''
  def __str__(self):
     return ('++ File not found. Check path.')

#def class os error
class FileError(Exception):
    def __init__(self, filename):
        self.filename = filename
        
    def __str__(self):
        return f"++ Error in accessing file: {self.filename}\n ++ Check path"

infile='hello.xlsx'
print('++ reading data')
try:
    df = pd.read_excel(infile)
# except Exception as e:
#     print('++ Invalid path provided ', e); sys.exit()

except Exception as e:
   print(FileError(infile), e); sys.exit()
#    print(NotValidPath(Exception), e); sys.exit()

# except:
#     raise FileError(infile)

# except:
#     print(FileError(infile)); sys.exit()