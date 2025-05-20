# Q2. After loading the DataFrame, how would you:
# Show column names?

# Check the number of rows and columns?

# Get a quick summary of numeric columns?

import pandas as pd

data = {
    'employee_id' : [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'department': ['HR', 'Finance', 'IT', 'Finance', 'IT'],
    'salary': [70000, 85000, 60000, 90000, 75000],
    'join_date': ['2019-04-23', '2018-05-15', '2020-01-30', '2017-08-10', '2021-11-01']
}

# Create DataFrame

df = pd.DataFrame(data)

# Save to CSV

df.to_csv('employees.csv', index=False) # Returns None

# Load the saved CSV

df = pd.read_csv('employees.csv')

# Show column names 

print("columns :",df.columns)

# Show the number of rows and columns 

print("Number of rows and columns", df.shape)

# Quick summary of numeric columns

print("Summary of numeric columns : \n",df.describe())






