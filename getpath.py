#!/usr/bin/env python3
"""
Created on Mon Jul 15 08:41:34 2019

Copyright (C) Jesse DeSimone, Ph.D.
"""
#%%

import os

dirpath = os.getcwd()
print("Path : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory : " + foldername)

#list directories and files within current working Directory
print('\n')
print('Directories and files')
for root, dirs, files in os.walk(".", topdown=True):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
