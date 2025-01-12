# Program to generate lowercased version of strings with length greater than five
strings = ['Python', 'is', 'a', 'great', 'language']
lowercased = [string.lower() for string in strings if len(string) > 5]
print(lowercased)
