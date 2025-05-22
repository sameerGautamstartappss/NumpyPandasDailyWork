# 🧪 Q2. Basic DataFrame Exploration
# After loading the DataFrame, perform the following:

# Show all column names

# Check the number of rows and columns

# Get a summary of numeric columns (such as scores and age)

import pandas as pd

dataset = pd.read_csv("students.csv") 

# Show all column names

print("Columns :",dataset.columns)

# Show the number of rows and columns 

print("Number of columns and rows :",dataset.shape)

# Get a summary of numeric columns 

print("Summary of numeric columns :\n",dataset.describe())

