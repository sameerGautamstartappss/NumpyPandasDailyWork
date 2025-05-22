# 🧪 Q3. Filtering Data
# Filter the students who meet both of the following criteria:

# Math score greater than 80

# City is "Delhi"


import pandas as pd

dataset = pd.read_csv("students.csv") # dataset to DataFrame

# Math score greater than 80

filtered_marks = dataset[(dataset['Math'] > 80) & (dataset['City']=="Delhi")]
print("Required marks are :\n", filtered_marks)