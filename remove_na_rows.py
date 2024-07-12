#!/usr/bin/env python3

# Import packages
import pandas as pd
import os

def remove_rows_with_na(df, columns):
    """
    Remove rows from the DataFrame where any of the specified columns contain NaN values.

    Parameters:
    df (pd.DataFrame): The DataFrame to clean.
    columns (list): A list of column names to check for NaN values.

    Returns:
    pd.DataFrame: The cleaned DataFrame with rows removed where any specified columns contain NaN values.
    """
    return df.dropna(subset=columns)

# Example usage
if __name__ == "__main__":
    # Create DataFrame
    os.chdir('/Users/jessedesimone/Desktop')
    df = pd.read_csv('infile.csv')

    # Specify columns to check for NaN values
    columns_to_check = df.columns[df.isna().any()].tolist() #finds any rows with n/a values

    # Remove rows with NaN values in specified columns
    cleaned_df = remove_rows_with_na(df, columns_to_check)

    print("\nCleaned DataFrame:")
    print(cleaned_df)

    # Export to csv
    cleaned_df.to_csv('cleaned_df.csv', index=False)
