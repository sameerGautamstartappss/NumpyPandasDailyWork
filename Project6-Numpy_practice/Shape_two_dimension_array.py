
# What is the shape of a 2D array and how do you find it?
import numpy as np

# Get the dimensions from the user 

rows = int(input("Enter the number of lists (rows): "))
cols = int(input("Enter the number of elements in each list(columns): "))

# Create a 2D list from the user

Matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter the {i+1} row and {j+1} column value: "))
        row.append(val)
    Matrix.append(row)

# Printing the list
print("Elements of the list are :", Matrix)

# Convert to numpy array 

arr = np.array(Matrix)

# Print the array

print("Elements of the numpy array are :\n", arr)

# Dimension of the array

print("Dimension of the array :", arr.ndim)

# Size of the array

print("Size of the array :", arr.size)

# Rank (Shape) of the array

print("Shape of the array :", arr.shape)

