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
        amount = float(input("Enter amount: "))
        expenses.append([name, amount])
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            for expense in expenses:
                print(expense[0], "-", expense[1])

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense[1]
        print("Total expenses:", total)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
