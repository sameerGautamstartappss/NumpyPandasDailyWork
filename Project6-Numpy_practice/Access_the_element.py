# How can you access the element at row 2, column 3 in a 2D array?

import numpy as np

# Get the dimensions from the user

rows = int(input("Enter the number of lists (rows): "))
cols = int(input("Enter the number of columns: "))

# Create a 2D list from the user

Matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter the {i+1} row and {j+1} column in the list : "))
        row.append(val)
    Matrix.append(row)

# Printing the list

print("Elements of the list are :\n", Matrix)

# Convert to numpy array

arr = np.array(Matrix)

# Print the array

print("Elements of the array are:\n", arr)

# Access the element at row 2 and column 3 in a 2D array

row = int(input("Enter the row of which you want the element: "))
col = int(input("Enter the column of which you want the element: "))

if (row-1) < rows and (col-1) < cols:
    print(f"Element at row {row} and column {col} :", arr[row-1][col-1])
else:
    print("Index out of bound")


