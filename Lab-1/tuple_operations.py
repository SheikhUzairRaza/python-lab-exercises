# Tuple Operations in Python

# Defining a tuple
pair = (3, 5)

# Accessing elements of a tuple by index
print(pair[0])  # Output: 3

# Tuple unpacking: Assigning tuple elements to variables
x, y = pair
print(x)  # Output: 3
print(y)  # Output: 5

# Tuples are immutable: Trying to modify a tuple element will raise an error
try:
    pair[1] = 6  # Attempting to change an element of the tuple
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment
