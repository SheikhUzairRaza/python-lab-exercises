# Program to count strings where first and last character are the same
sample_list = ["abc", "xyz", "aba", "1221"]
count = 0

for string in sample_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print(f"Count of strings with same first and last character: {count}")
