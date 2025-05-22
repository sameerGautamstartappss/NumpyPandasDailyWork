# 🧪 Q4. Calculate Average Score
# Calculate the average score of each student across the subjects Math, Science, and English.

# Hint: Add a new column called average_score to the DataFrame.

import pandas as pd

dataset = pd.read_csv("students.csv") # Converted dataset to DataFrame

dataset['average'] = (dataset['Math'] + dataset['Science'] + dataset['English'])/3

dataset['status'] = "active"

print("Summary of numeric columns :\n", dataset.describe())