import pandas as pd
from scipy.spatial import cKDTree

# Load the Excel file
file_path = '/Users/jessedesimone/Desktop/test.xlsx'
conv_df = pd.read_excel(file_path, sheet_name='CONV')
nconv_df = pd.read_excel(file_path, sheet_name='NCONV')

# Define matching function
def match_subjects(conv_df, nconv_df, variables=['CDR', 'AGE', 'SEX']):
    matches = []
    unmatched = nconv_df.copy()
    
    for _, row in conv_df.iterrows():
        # Prioritize CDR (exact match)
        cdr_matches = unmatched[unmatched['CDR'] == row['CDR']]
        
        # Prioritize AGE (nearest match)
        if not cdr_matches.empty:
            # Calculate AGE difference and find the closest match
            cdr_matches = cdr_matches.copy()
            cdr_matches['AGE_diff'] = (cdr_matches['AGE'] - row['AGE']).abs()
            closest_match = cdr_matches.loc[cdr_matches['AGE_diff'].idxmin()]
        else:
            closest_match = unmatched.loc[(unmatched['CDR'] == row['CDR']) & 
                                          (unmatched['SEX'] == row['SEX'])].iloc[0]
        matches.append(closest_match)
        unmatched = unmatched.drop(closest_match.name)
    matched_nconv_df = pd.DataFrame(matches)
    return matched_nconv_df

matched_nconv_df = match_subjects(conv_df, nconv_df)
matched_nconv_df.to_excel('/Users/jessedesimone/Desktop/matched.xlsx')
