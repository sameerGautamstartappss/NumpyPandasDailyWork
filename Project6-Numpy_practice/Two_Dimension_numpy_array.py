# How do you create a 2D NumPy array from a list of lists?

import numpy as np

# Lambda to create a 2D list
row = int(input("Enter the number of lists in the list : "))
column = int(input("Enter the number of elements in each list : "))

# Taking the input of 2-D list and then converting it into the numpy array
arr = (np.array((lambda row, column : list(list(int(input(f"Enter the {j+1} row and {i+1} element : ")) for i in range(column)) for j in range(row)))(row, column)))

# Get the elements of the list 
# print("Elements of the list are :", List1)

# Coverting the list into array using array() function of numpy

# arr = np.array(List1)

# Printing the elements of the array

print(arr)

# Get the dimensions of the array

print("Dimension of arr :", arr.ndim)