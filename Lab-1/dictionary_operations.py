# Dictionary Operations in Python

# Defining a dictionary with student IDs
studentIds = {'knuth': 42.0, 'turing': 56.0, 'nash': 92.0}

# Accessing a value using a key
print(studentIds['turing'])  # Output: 56.0

# Modifying the value associated with a key
studentIds['nash'] = 'ninety-two'
print(studentIds)  # Output: {'knuth': 42.0, 'turing': 56.0, 'nash': 'ninety-two'}

# Deleting an element from the dictionary using its key
del studentIds['knuth']
print(studentIds)  # Output: {'turing': 56.0, 'nash': 'ninety-two'}

# Adding a new key-value pair to the dictionary
studentIds['knuth'] = [42.0, 'forty-two']
print(studentIds)  # Output: {'turing': 56.0, 'nash': 'ninety-two', 'knuth': [42.0, 'forty-two']}

# Retrieving the keys of the dictionary
print(studentIds.keys())  # Output: dict_keys(['turing', 'nash', 'knuth'])

# Retrieving the values of the dictionary
print(studentIds.values())  # Output: dict_values([56.0, 'ninety-two', [42.0, 'forty-two']])

# Retrieving the key-value pairs (items) of the dictionary
print(studentIds.items())  # Output: dict_items([('turing', 56.0), ('nash', 'ninety-two'), ('knuth', [42.0, 'forty-two'])])

# Getting the number of key-value pairs in the dictionary
print(len(studentIds))  # Output: 3
