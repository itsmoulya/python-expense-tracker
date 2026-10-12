import json
import os

FILE_NAME = "expenses.json"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        expenses = json.load(file)
else:
    expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")

        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            expenses.append([name, amount])

            with open(FILE_NAME, "w") as file:
                json.dump(expenses, file, indent=4)

            print("Expense added and saved!")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            for expense in expenses:
                print(expense[0], "-", expense[1])

    elif choice == "3":
        total = sum(expense[1] for expense in expenses)
        print("Total expenses:", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
