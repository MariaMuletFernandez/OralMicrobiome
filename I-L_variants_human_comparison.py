# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:53:25 2024

This script takes an excel file with the peptides data that we want to search of I/L variants. The excel input should have only
3 columns: Proteins, the raw peptides and the clean peptides (without any symbol or PTM information, inly the aminoacids). The script will
take the excel, find for the I/L variants of the peptides, compare them with the human proteome DDB and generate a new excel file with two
more columns: the variants and if they are or not in the human proteome.

@author: María Mulet Fernández
"""

# Import the libraries
import pandas as pd

# Prompt the user for the file path of the Excel file
DDBB_path = input("Enter the file path of the DDBB file: ")

# Reading proteome file:
try:
    with open(DDBB_path, 'r') as proteome_file:
        content = proteome_file.read()
        print("DDBB file successfully loaded into DataFrame.")
except Exception as e:
    print(f"An error occurred while trying to read the DDBB file: {e}")


# Prompt the user for the file path of the Excel file
file_path = input("Enter the file path of the Excel file: ")

# Read the Excel file into a DataFrame
try:
    df = pd.read_excel(file_path)
    print("Excel file successfully loaded into DataFrame.")

except Exception as e:
    print(f"An error occurred while trying to read the Excel file: {e}")
    
#Create an empty df with the following columns:
df2 = pd.DataFrame(columns=['Protein', 'Peptide','Variants','Human'])

#Saves the number of rows and columns:
row_count = df.shape[0]
col_count = df.shape[1]
    
# Setting the first row of the excel for writing in it.
N = 2

# Go across the rows:
for current_row in range(1, row_count):
        peptide = df.iloc[current_row, 3]
        p_accesion = df.iloc[current_row, 0]
        
        l_1 = [""]
        
        # Generating a list of all variants:
        for c in peptide:
            if c != "L" and c != "I":
                for pos in range(0, len(l_1)):
                    l_1[pos] += c
                            
            else:
                l_2 = l_1.copy()
        
                for pos in range(0, len(l_1)):
                    l_1[pos] += "L"
                
                for pos in range(0, len(l_2)):
                    l_2[pos] += "I"
                l_1 = l_1 + l_2
        
        # Writing the variants and the original peptide in the new df:
        for pep in l_1:
            
            pep_original = "".join(peptide)
                
            if pep in content:
                df2.loc[df2.shape[N]] = [str(p_accesion),pep_original,pep,'YES'] #There is only added the data of the protein
                                                                            #accession, the original sequence of the peptide, the variants
                                                                            #and in if those are in the human proteome or not.
                N += 1
            else:
                df2.loc[df2.shape[N]] = [str(p_accesion),pep_original,pep,'NO']
                N += 1
        
        
# Prompt the user for the file path of the Excel file
output_path = input("Enter the file path of the output file: ")

# Save the new data frame as an excel file:
try:
    df2.to_excel(output_path, index = False)
    print("Output Dataframe successfully saved as Excel file.")

except Exception as e:
    print(f"An error occurred while trying to save the Excel file: {e}")

