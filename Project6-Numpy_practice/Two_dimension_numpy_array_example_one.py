import numpy as np 

# Get dimensions from the user

rows = int(input("Enter the number of lists (rows): "))
cols = int(input("Enter the number of elements in each list (columns): "))

# Create a 2-D list from the user 

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Enter the {i+1} row and {j+1} column value : "))
        row.append(val)
    matrix.append(row)

# Print the list of lists

print("Elements of the list are :", matrix)

# Convert to numpy array

arr = np.array(matrix)

# Print the array

print("Elements of the numpy array are :\n", arr)

# Print the dimension of the array

print("Dimension of the array :", arr.ndim)
