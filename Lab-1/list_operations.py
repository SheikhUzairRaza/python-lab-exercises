# List Operations in Python

# Defining a list of fruits
fruits = ['apple', 'orange', 'pear', 'banana']
print(fruits[0])  # Output: 'apple' (Accessing the first element)

# List Concatenation: Joining two lists
otherFruits = ['kiwi', 'strawberry']
print(fruits + otherFruits)  # Output: ['apple', 'orange', 'pear', 'banana', 'kiwi', 'strawberry']

# Negative Indexing: Accessing elements from the end of the list
print(fruits[-2])  # Output: 'pear' (Second to last element)

# Pop: Removing and returning the last element of the list
print(fruits.pop())  # Output: 'banana' (Last element removed)
print(fruits)  # Output: ['apple', 'orange', 'pear'] (List after pop)

# Modifying Lists:
# Append: Adding a new element to the end of the list
fruits.append('grapefruit')
print(fruits)  # Output: ['apple', 'orange', 'pear', 'grapefruit']

# Update an existing element
fruits[-1] = 'pineapple'  # Replacing 'grapefruit' with 'pineapple'
print(fruits)  # Output: ['apple', 'orange', 'pear', 'pineapple']

# List Slicing: Extracting portions of the list
print(fruits[0:2])  # Output: ['apple', 'orange'] (Elements from index 0 to 1)
print(fruits[:3])  # Output: ['apple', 'orange', 'pear'] (Elements from the start to index 2)
print(fruits[2:])  # Output: ['pear', 'pineapple'] (Elements from index 2 to the end)

# Length of the list
print(len(fruits))  # Output: 4 (Number of elements in the list)

# Lists of Lists (Nested lists)
lstOfLsts = [['a', 'b', 'c'], [1, 2, 3], ['one', 'two', 'three']]
print(lstOfLsts[1][2])  # Output: 3 (Accessing the 3rd element of the second sublist)

# Pop from a nested list
print(lstOfLsts[0].pop())  # Output: 'c' (Popping the last element of the first sublist)
print(lstOfLsts)  # Output: [['a', 'b'], [1, 2, 3], ['one', 'two', 'three']] (Updated list of lists)
