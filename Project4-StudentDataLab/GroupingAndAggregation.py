# Q5. Grouping and Aggregation
# Group students by their City and:

# Show the average Math score for each city

# Show the count of students in each city

import pandas as pd

# Load the CSV to make DataFrame

dataset = pd.read_csv("students.csv")

average_math_score = lambda city : 