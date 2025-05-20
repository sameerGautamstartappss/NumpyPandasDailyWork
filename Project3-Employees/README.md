# Employee Data Analysis with Pandas

This project demonstrates how to work with employee data using the pandas library in Python. It covers loading data, inspecting the DataFrame structure, and summarizing numeric columns.

---

## Overview

You have a dataset containing employee information with the following fields:

- `employee_id`: Unique identifier for each employee
- `name`: Employee name
- `department`: Department name where the employee works
- `salary`: Employee salary
- `join_date`: The date the employee joined the company

The data is saved into a CSV file, then loaded back into a pandas DataFrame for analysis.

---

## Objectives

After loading the DataFrame from the CSV file, perform the following tasks:

1. **Show column names**  
   Display the list of column headers in the DataFrame to understand the data structure.

2. **Check the number of rows and columns**  
   Determine the shape of the DataFrame to know how many records and features it contains.

3. **Get a quick summary of numeric columns**  
   Generate descriptive statistics such as count, mean, standard deviation, minimum, and maximum for all numeric columns.

---

## How to Run

1. Make sure you have Python 3.x installed.

2. Install pandas if you haven’t already:

   ```bash
   pip install pandas
