# Exercise 1: Volume Calculation & Categorization
height = int(input("Enter height: "))
width = int(input("Enter width: "))
depth = int(input("Enter depth: "))
volume = height * width * depth

if 1 <= volume <= 10:
    print("Extra Small")
elif 11 <= volume <= 25:
    print("Small")
elif 26 <= volume <= 75:
    print("Medium")
elif 76 <= volume <= 100:
    print("Large")
elif 101 <= volume <= 250:
    print("Extra Large")
else:
    print("Extra-Extra Large")
