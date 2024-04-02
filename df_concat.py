#!/usr/bin/env python3
'''
Module for reading csv data file and concatenating dataframes
Here have the same dataframes in 2 separate directories and want to concat the data from each of the dataframes

'''
import os
import pandas as pd

os.chdir('/Users/jessedesimone/Desktop')    #set cwd

#locations of two directories (each directory contains the same filenames)
path1=os.getcwd() + '/' +'Compile_ROI_240401'
path2=os.getcwd() + '/' +'Compile_ROI_240402'

#create the output directory for new files
output_dir=os.getcwd() + '/' +'combined_dataframes'
if os.path.exists(output_dir):
    print('Outdir exists already >>> exiting')
    #exit()
else:
    print('Outdir does not exist >>> creating')
    os.makedirs(output_dir)


dataframe_list=['GRP_ROI_means_FA.csv', 
                'GRP_ROI_means_FW.csv', 
                'GRP_ROI_means_MD.csv', 
                'GRP_ROI_means_L2.csv', 
                'GRP_ROI_means_L3.csv', 
                'GRP_ROI_means_L1.csv', 
                'GRP_ROI_means_fwcFA.csv', 
                'GRP_ROI_means_fwcMD.csv', 
                'dmri_input.csv', 
                'GRP_ROI_means_fwcL2.csv', 
                'GRP_ROI_means_fwcL3.csv', 
                'GRP_ROI_means_fwcL1.csv']

# Iterate through each list and create a new file
for df in dataframe_list:
    print('concatenating files for', df)
    df1_path=path1 + '/' + df
    df1=pd.read_csv(df1_path)
    df2_path=path2 + '/' + df
    df2=pd.read_csv(df2_path)
    frames=[df1, df2]
    df_concat=pd.concat(frames, axis=0)
    df_concat.to_csv(output_dir  + '/' + df, index=False)






