"""
Module for parsing text from Quote pdf

Functions:
    -reads pdf file using {str} input </path/to/file> and {str} input filename.pdf
    -creates output text file filename.txt

Change Log
==========
0.0.1 (2021-03-24)
-Version 1
---------

#TO-DO
Try to clean up whitespace
"""

import os
from pdfminer import high_level
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

fpath = input('\nSpecify </path/to/file/>')
print(os.listdir(prompt1))
fname = input('\nEnter file name: ')
infile = fpath + fname
print('File selected: ' + infile)

output_string = StringIO()
with open(infile, 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

print(output_string.getvalue())


outname = fname[0:-4]

f = open(fpath + outname + '.txt', 'a')
encrypt = pdf_reader.getIsEncrypted() # returns if the pdf is encrypted or not
print('Encrypted: ', encrypt, file = f)
pages = pdf_reader.getNumPages() # returns number of pages in the pdf
print ('Pages: ', pages, file = f)
print(output_string.getvalue().lstrip(), file = f)
f.close()
