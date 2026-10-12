import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read saved expenses.")
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


expenses = load_expenses()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Monthly Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Expense name: ")
        category = input("Category (Food/Travel/Books/Other): ")

        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            expense = {
                "name": name,
                "category": category,
                "amount": amount,
                "date": datetime.now().strftime("%Y-%m-%d")
            }

            expenses.append(expense)
            save_expenses(expenses)
            print("Expense saved successfully!")

        except ValueError:
            print("Enter a valid amount.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            for item in expenses:
                print(
                    item["date"], "|",
                    item["name"], "|",
                    item["category"], "| ₹",
                    item["amount"]
                )

    elif choice == "3":
        total = sum(item["amount"] for item in expenses)
        print("Total expenses: ₹", round(total, 2))

    elif choice == "4":
        month = datetime.now().strftime("%Y-%m")
        monthly = [
            item for item in expenses
            if item["date"].startswith(month)
        ]
        total = sum(item["amount"] for item in monthly)

        print("Monthly report:", month)
        print("Number of expenses:", len(monthly))
        print("Total spent: ₹", round(total, 2))

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
