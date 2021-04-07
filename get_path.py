#!/usr/bin/env python3
'''
Module for listing all subdirectories and files within a given directory

Change Log
=========
0.0.1 (2021-04-07)
--------
Initial commit
'''

import os
def get_dir():
   dir_path = os.getcwd()
   print('ROOT Directory: ', dir_path)
   print('\nList Directory: ')
   print(os.listdir())
   for root, dirs, files in os.walk(".", topdown=True):
      for name in files:
         print(os.path.join(root, name))
      for name in dirs:
         print(os.path.join(root, name))

if __name__ == '__main__':
   get_dir()