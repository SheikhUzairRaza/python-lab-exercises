# Exercise 1: Worker Efficiency
time_taken = float(input("Enter time taken by worker (in hours): "))
if 2 <= time_taken < 3:
    print("Highly efficient")
elif 3 <= time_taken < 4:
    print("Needs to improve speed")
elif 4 <= time_taken < 5:
    print("Needs training")
else:
    print("Worker has to leave the company")


