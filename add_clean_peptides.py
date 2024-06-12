# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:29:47 2022

This script takes as an input an excel file with your peptide information. It must have a column with the raw peptides data, which means
that the aminoacid sequences include some symbols or PTM information that you want to remove in order to later generate the variants and
compare with the human proteome using the script 'I-L_variants_human_comparison.py'.

@author: Maria Mulet Fernández
"""

import pandas as pd

# Prompt the user for the file path of the Excel file
file_path = input("Enter the file path of the Excel file: ")

# Read the Excel file into a DataFrame
try:
    df = pd.read_excel(file_path)
    print("Excel file successfully loaded into DataFrame.")

except Exception as e:
    print(f"An error occurred while trying to read the Excel file: {e}")

#df = pd.read_excel("//irb218.udl.net/pprg.MSNAS01/MMulet/LncRNA_study/Análisis María/raw_data/D_features.xlsx")

df.insert(2, 'Clean peptides', "") # Adding new empty column 'clean peptides' as the third column

peptide = input("Enter the name of the column that has the peptide information: ") #Creates a variable with the peptides column name.

for i in range(len(df)): #Loop to iterate over each df 
        pep = df.loc[i,peptide] #Getting each peptide
        
        pep_i = ''.join(filter(str.isalpha, pep)) #Cleaning peptides
        pep_f = pep_i[1:-1]
        
        df.loc[i, 'Clean peptides'] = pep_f #Add clean peptides
        

# Prompt the user for the file path of the Excel file
output_path = input("Enter the file path of the output file: ")

# Save the new data frame as a new excel file:
try:
    df.to_excel(output_path, index = False)
    print("Output Dataframe successfully saved as Excel file.")

except Exception as e:
    print(f"An error occurred while trying to save the Excel file: {e}")

