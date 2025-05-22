# 🧪 Q1. Load the Dataset
# You have a CSV file named "students.csv".

# Load it into pandas and show the first 5 rows.

import pandas as pd


# Load CSV file
dataset = pd.read_csv("students.csv") # pd.read_csv() reads the CSV file "students.csv" and returns a pandas DataFrame.
# dataset is storing the DataFrame in the variable.
# So, dataset refers to a DataFrame, which is your in-memory dataset.
# Now 'dataset' is a DataFrame

# In other words:
    # Before the line runs: "students.csv is a file on a disk"
    # After the line runs: "dataset" becomes a pandas DataFrame, which is a structured dataset in python memory(rows and columns, like a table)

# Dataset - Collection of data, usually tabular
# DataFrame - pandas object representing the dataset
# CSV file - Common format used to store datasets

print(dataset.head())