# Sales Data Example with Pandas

This project demonstrates how to create a sample sales dataset, save it as a CSV file, load the CSV back into a pandas DataFrame, and display the first 5 rows.

---

## Overview

- Create a sales dataset with columns: `region`, `sales`, and `date`.
- Save the dataset to a CSV file named `sales.csv`.
- Load the CSV file back into a DataFrame.
- Display the first 5 rows of the loaded data.

---

## Code Explanation

```python
import pandas as pd

# Step-1: Create sample data
data = {
    'region': ['West', 'East', 'North', 'South', 'West'],
    'sales': [6000, 4000, 3000, 7000, 8000],
    'date': ['2023-01-01', '2023-01-03', '2023-01-05', '2023-01-07', '2023-01-09']
}

# Step-2: Create DataFrame
df = pd.DataFrame(data)

# Step-3: Save DataFrame to CSV
df.to_csv('sales.csv', index=False)

# Step-4: Load the CSV file
df_loaded = pd.read_csv('sales.csv')

# Step-5: Show the first 5 rows
print(df_loaded.head())
