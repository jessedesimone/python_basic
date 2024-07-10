#!/usr/local/bin/python3.9

'''code to create directory if is does not yet exist'''

# create output directory
import os
def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
    else:
        print(f"Directory '{directory_path}' already exists.")

directory_path = '/Users/jessedesimone/Desktop/LME_RESULTS'
create_directory(directory_path)