# Exercise 1: Username & Password Check
username = input("Enter username: ")
password = input("Enter password: ")
if password.lower() == "abc$123":
    print("Welcome!")
else:
    print("I don't know you.")
