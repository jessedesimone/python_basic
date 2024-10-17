#!/usr/bin/env python3

'''
Module for random sample with replacement to achieve the desired conditions
'''

# Import packages
import pandas as pd
import numpy as np

# Assuming `df2` is your DataFrame

# Set the desired parameters
num_cases = 32
desired_avg_age = 70
desired_female_ratio = 0.40

# Create a random sample with replacement to achieve the desired conditions
for _ in range(1000):
    sample = df2.sample(n=num_cases, replace=False)
    
    # Calculate the average age and female ratio of the sample
    avg_age = sample['Age'].mean()
    female_ratio = sample['Sex'].mean()  # Assuming Sex=1 for female, 0 for male
    
    # Check if the sample meets the desired conditions
    if abs(avg_age - desired_avg_age) <= 5 and abs(female_ratio - desired_female_ratio) <= 5:
        break
    
    # Provide feedback if it took too many iterations
    else:
        print("Unable to find an ideal sample after 1000 iterations, using the closest match.")

print("Sampled DataFrame:")
print(sample)
print(f"Average Age: {avg_age}")
print(f"Female Ratio: {female_ratio:.2f}")

# Ensure you have the correct number of rows
assert len(sample) == num_cases, "Sample size does not match the specified number of cases"