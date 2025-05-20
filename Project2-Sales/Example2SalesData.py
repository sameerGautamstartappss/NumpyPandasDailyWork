# Q2. You have a CSV file named "sales.csv". Load it into pandas and show the first 5 rows.

import pandas as pd

# Step-1: Create sample Data

data = {
    'region': ['West', 'East', 'North', 'South', 'West'],
    'sales': [6000, 4000, 3000, 7000, 8000],
    'date': ['2023-01-01', '2023-01-03', '2023-01-05', '2023-01-07', '2023-01-09']
}

# Step-2: Create Dataframe

df = pd.DataFrame(data)

## A DataFrame is like a smart table - think of it as an Excel sheet but inside python, with superpowers

## It helps us:
    # Organize structured data (rows and columns).
    # performs analysis efficiently.
    # Clean, filter, group, and manipulate data.
    # Export or visualize data easily.  

## Real-world use cases of a DataFrame

    # Reading data from files 
        # Load CSV, Excel, SQL, JSON,etc into a clean table format.
        # Example: Loading "sales.csv" to analyze sales data.
    # Data Cleaning
        # Handle missing values, fix column names, correct data types.
        # Example- Remove rows where sales = 0 or data is missing
    # filtering and Querying
        # find all rows where sales > 5000
        # Compare performance by region
    # Aggregation and grouping 
        # Total sales per region
        # Average monthly sales 
    # Merging Data 
        # Combining data from multiple sources: products + sales + customer info
    # Exporting reports
        # Save your cleaned or transformed data to csv, excel, or database

# Step-3: Save DataFrame to CSV
df.to_csv('sales.csv', index=False)

# Step-4: Load it back (just to test)
df_loaded = pd.read_csv('sales.csv')

# Step-5: Show first five rows
print(df_loaded.head())
