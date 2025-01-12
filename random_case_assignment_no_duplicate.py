
'''
Number of Neurologists: 21, each with a unique ID.
Number of Cases: 99, each with a unique patient ID.
Assignment Rule: Each neurologist will review 3 cases per run, ensuring no case is reassigned to the same neurologist.

Output: An Excel file to track assignments, including:
Neurologist ID
Assigned patient IDs
Date of assignment

Input: The script can read from the Excel file to avoid reassigning previously assigned cases to a neurologist.
Checks if the Excel file exists (For first time, run with no input)
If no prior Excel file exists, the script initializes assignments from scratch.
If the file exists (filepath), it reads past assignments and avoids duplicates.
It updates the Excel file with new assignments after every run.

'''
# Import packages
import pandas as pd
import random
from datetime import datetime

def assign_cases(file_path):
    # Constants
    neurologist_ids = list(range(1, 22))  # IDs from 1 to 21; Replace this with alphanumeric neurologist IDs
    patient_ids = list(range(1, 100))  # IDs from 1 to 99; Replace this with list of cases
    date_today = datetime.today().strftime('%Y-%m-%d')

    try:
        # Load existing assignments if the file exists
        assignments = pd.read_excel(file_path)
    except FileNotFoundError:
        # Initialize empty DataFrame if file doesn't exist
        assignments = pd.DataFrame(columns=['Neurologist ID', 'Patient ID', 'Date Assigned'])

    # Create a dictionary to track assigned cases for each neurologist
    assigned_cases = {nid: set(assignments[assignments['Neurologist ID'] == nid]['Patient ID'].tolist()) for nid in neurologist_ids}

    # New assignments list
    new_assignments = []

    for nid in neurologist_ids:
        available_cases = list(set(patient_ids) - assigned_cases[nid])

        if len(available_cases) < 3:
            raise ValueError(f"Not enough available cases to assign to neurologist {nid}.")

        selected_cases = random.sample(available_cases, 3)

        for case in selected_cases:
            new_assignments.append({'Neurologist ID': nid, 'Patient ID': case, 'Date Assigned': date_today})

    # Add new assignments to the DataFrame
    new_assignments_df = pd.DataFrame(new_assignments)
    updated_assignments = pd.concat([assignments, new_assignments_df], ignore_index=True)

    # Save to Excel with date in filename
    output_file = file_path.replace('.xlsx', f'_{date_today}.xlsx')
    updated_assignments.to_excel(output_file, index=False)
    print(f"New assignments saved to {output_file}")

# Usage
assign_cases("case_assignment_tracker_2025-01-12.xlsx")
