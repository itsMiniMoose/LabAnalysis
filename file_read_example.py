"""
Description: 
The following is a basic example script that demonstrates reading in excel 
and csv data into a pandas dataframe. 

Dependencies:
    - pandas
    - numpy
    - os (standard library)
    - openpyxl
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                               Imports
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd 
import numpy as np 
import os
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# operation to get string of current directory path
current_directory = os.getcwd()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Excel example:
xlsx_file_name = "06-13-23a_idle.xlsx"
xlsx_path = current_directory + '/' + xlsx_file_name

df1 = pd.read_excel(xlsx_path, skiprows=[0, 1, 2, 3, 5])
print(df1.head())


# CSV example:
csv_file_name = "06-13-23a_idle.csv"
csv_path = current_directory + '/' + csv_file_name

df2 = pd.read_csv(csv_path, skiprows=[0, 1, 2, 3, 5])
print(df2.head())
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" Once you have your dataframe (df) you can now index the data via python and 
pandas. Look into pandas to learn more about all of the features but here are a 
few examples ...
"""

# print all temperatures in a given column:
temp1_list = df2["Temp 1:"]
print(f"Oven Temperatures: \n{temp1_list}")

# take an average of temperature values from row 50 to end of list (method 1)
avg_temperature1 = round(df2["Temp 1:"][50:].mean(), 2)
print(f"Average Oven Temperature: {avg_temperature1} F")

# take an average of temperature values from row 50 to end of list (method 1)
avg_temperature2 = round(df2.iloc[50:, 11].mean(), 2)
print(f"Average Oven Temperature: {avg_temperature2} F")

# Sum the energy values in a list over a specified range
energy = df2.iloc[50:, 5].sum()
print(f"Energy: {energy} Wh")
