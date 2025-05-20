# Student Data Analysis

This project demonstrates a simple workflow for creating, saving, reading, and exploring student data using **pandas** in Python.

---

## Project Structure

- `script.py`  
  Creates a sample dataset of students with their scores and saves it as a CSV file.

- `step1_read_csv.py`  
  Contains a reusable function to read a CSV file into a pandas DataFrame.

- `step2_explore_data.py`  
  Reads the saved CSV file and performs basic exploratory data analysis, including:  
  - Displaying the first 5 rows  
  - Showing DataFrame info  
  - Showing statistical summary of numeric columns

---

## How to Use

1. **Create and save the data**  
   Run `script.py` to create the student data and save it as `students.csv`.

   ```bash
   python script.py
