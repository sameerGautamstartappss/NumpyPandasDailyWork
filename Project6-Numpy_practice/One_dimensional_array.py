import numpy as np

# lambda to take the input of the elements in a list

list1 = (lambda num : list(int(input(f"Enter the {i+1} elements in the list : ")) for i in range(num)))(int(input("Enter the number of elements in the list : ")))

arr = np.array(list1) # Using the array() function of numpy to generate the ndarray

# printing the elemnts of the ndarray
print(arr)

# printing the type of arr 

print(type(arr))

# Get the number of dimensions of arr
print("Dimension of arr :",arr.ndim)