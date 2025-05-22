import numpy as np

# lambda to take the input of the elements in a list
list1 = (lambda num : list(int(input(f"Enter the {i+1} element in the list: ")) for i in range(num)))(int(input("Enter the number of elements in the list: ")))

arr = np.array(list1) # Creating numpy "ndarray" using array() function of numpy

print(arr) # printing the numpy ndarray object

print(type(arr)) # printing the type of array object
