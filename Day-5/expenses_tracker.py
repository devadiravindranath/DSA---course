expenses = []

def show_menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

def add_expense():
    name = input("Enter expense name: ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully.")

def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n----- Expenses List -----")
    total = 0

    for expense in expenses:
        print(f"{expense['name']} - ₹{expense['amount']}")
        total += expense["amount"]

    print(f"Total expense: ₹{total}")

def main():
    while True:
        show_menu()
        choice = input("Enter the choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Exiting.... Thank you")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
