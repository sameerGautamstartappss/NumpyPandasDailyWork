import numpy as np

# lambda to take the input of the tuples

Tuple1 = (lambda num : tuple(int(input(f"Enter the {i+1} element of the tuple : ")) for i in range(num)))(int(input("Enter the number of elements of the tuple : ")))

# Get the elements of the tuple
print("Elements of the tuple are :",Tuple1)
arr = np.array(Tuple1)

# print the elements of the ndarray

print(arr) 

# print the type of arr

print(type(arr))