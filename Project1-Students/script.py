import pandas as pd

#  Step-1: Create data 
data = {
    "Name": ["Alice", "bob", "Charlie", "David", "Eva"],
    "Age": [15, 16, 15, 16, 15],
    "Math": [88, 75, 90, 60, 95],
    "Science": [92, 78, 85, 65, 91],
    "English": [85, 80, 87, 58, 94],
    "City": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai"]
}

# Step-2: Convert to dataframe

df = pd.DataFrame(data)

# Step-3: Save it as a csv file

df.to_csv("students.csv", index=False) 