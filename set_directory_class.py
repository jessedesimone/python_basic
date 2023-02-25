#!/usr/bin/env python3
# configure directories

import os
class directories:
    '''Should be accessible in each module'''
    base_dir = '/Users/jessedesimone/Documents/' 
    sub_dir = os.path.join(base_dir, 'postdoc_uf/')

print("Listing directory: {}".format(directories.sub_dir))
print(os.listdir(directories.sub_dir))