# ATM System Simulation

# Task 1: Introduction
def atm_intro():
    print("Welcome to the Python ATM System!")

# Task 2: Terminal
def display_options():
    print("\nPlease choose an option:")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. View Transaction History")
    print("5. Exit")

# Task 3: Python Interpreter
# This section interacts with the user through the command line interface

# Task 4: Variables
balance = 1000  # Starting balance
transaction_history = []  # To store the history of transactions

# Task 5: Text Editor
# This is covered as comments throughout the code

# Task 6: Functions
def check_balance():
    """Returns the current balance."""
    return balance

def deposit(amount):
    """Deposit funds to the account."""
    global balance
    balance += amount
    transaction_history.append(f"Deposited: ${amount}")

def withdraw(amount):
    """Withdraw funds from the account."""
    global balance
    if amount <= balance:
        balance -= amount
        transaction_history.append(f"Withdrew: ${amount}")
    else:
        print("Insufficient funds!")

# Task 7: Lists and Tuples
# Using list to store transaction history and tuple for balance-related info
def view_transaction_history():
    """Prints the transaction history."""
    if transaction_history:
        print("\nTransaction History:")
        for transaction in transaction_history:
            print(transaction)
    else:
        print("No transactions found.")

# Task 8: Conditional Statements
# Conditional statements are used to ensure valid input and transactions
def perform_action(choice):
    """Performs action based on user choice."""
    if choice == 1:
        print(f"Current balance: ${check_balance()}")
    elif choice == 2:
        amount = float(input("Enter amount to deposit: $"))
        deposit(amount)
        print(f"${amount} deposited successfully!")
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: $"))
        withdraw(amount)
    elif choice == 4:
        view_transaction_history()
    elif choice == 5:
        print("Thank you for using the ATM system. Goodbye!")
        return False
    else:
        print("Invalid choice, please try again.")
    return True

# Task 9: The For Loop
# The for loop is used to print out transaction history

# Task 10: User Input and the While Loop
def atm_system():
    """Runs the ATM system."""
    atm_intro()
    
    while True:
        display_options()
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue
        
        if not perform_action(choice):
            break  # Exit the while loop when the user chooses option 5

# Start the ATM system
atm_system()
