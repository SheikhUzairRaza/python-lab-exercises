# Program to concatenate dictionaries

# Defining three dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenating the dictionaries using dictionary unpacking (Python 3.5+)
concatenated_dict = {**dic1, **dic2, **dic3}

# Output the concatenated dictionary
print(concatenated_dict)