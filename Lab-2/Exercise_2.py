# Exercise 2: Print numbers from 0 to 100
for i in range(101):
    print(i)

# Multiplication Table
num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Numbers 1 to 10 in Reverse
for i in range(10, 0, -1):
    print(i)

# Count Even Numbers to 10
for i in range(2, 11, 2):
    print(i)

# Sum numbers from 100 to 200
total = sum(range(100, 201))
print("Sum from 100 to 200:", total)

# List Countries Using While Loop
countries_list = ["Canada", "USA", "Mexico"]
i = 0
while i < len(countries_list):
    print(countries_list[i])
    i += 1

# Demonstrate Nested Loops
for i in range(1, 4):
    j = 1
    while j <= 3:
        print(f"Nested Loop: i={i}, j={j}")
        j += 1