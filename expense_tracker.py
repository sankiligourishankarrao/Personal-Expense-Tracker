"""Personal Expense Tracker: a menu-driven command-line program.

Add, view (with a date or category filter), delete, and summarize expenses,
and save them to / load them from a text file.

Run:  python3 expense_tracker.py
"""
import os

DATA_FILE = 'expenses.txt'

expenses = []
next_id = 1


def add_Expense(date, amount, category, description):
    global next_id
    expense = {
        'id': next_id,
        'date': date,
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)
    next_id += 1
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expense recorded.")
        return
    filter_choice = input("Do you want to filter by (1) Date or (2) Category? (Enter '1', '2' or '0' for none): ")
    if filter_choice == '1':
        filter_date = input('Enter the date to filter (YYYY-MM-DD): ')
        filtered_expenses = [expense for expense in expenses if expense['date'] == filter_date]
    elif filter_choice == '2':
        filter_category = input('Enter the category to filter: ')
        filtered_expenses = [expense for expense in expenses if expense['category'].lower() == filter_category.lower()]
    else:
        filtered_expenses = expenses
    if not filtered_expenses:
        print("No expenses found for the given filter.")
    for expense in filtered_expenses:
        print(f"ID : {expense['id']}, Date : {expense['date']}, Amount : {expense['amount']}, "
              f"Category : {expense['category']}, Description : {expense['description']}")


def delete_expense(expense_id):
    index = 0
    for i in expenses:
        if i['id'] == expense_id:
            expenses.pop(index)
            print("Expense deleted successfully!")
            return
        index += 1
    print("Given expense id is not present.")


def generate_summary():
    summary = {}
    for expense in expenses:
        category = expense['category']
        summary[category] = summary.get(category, 0) + expense['amount']
    for category, amount in summary.items():
        print(f"Category: {category}, Total Amount: {amount}.")


def save_expenses_to_file(filename):
    with open(filename, 'w') as file:
        for expense in expenses:
            file.write(f"{expense['id']}, {expense['date']}, {expense['amount']}, {expense['category']}, {expense['description']}\n")
    print("Expenses saved to file.")


def load_expenses_from_file(filename):
    global next_id
    # Fix: on the first run there is no file yet, so start with an empty list instead of crashing.
    if not os.path.exists(filename):
        return
    with open(filename, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            # Fix: the file is written with ", " between fields, so strip each field to drop the extra space.
            # maxsplit=4 keeps any commas inside the description.
            id, date, amount, category, description = [part.strip() for part in line.split(',', 4)]
            expenses.append({
                'id': int(id),
                'date': date,
                'amount': float(amount),
                'category': category,
                'description': description
            })
            next_id = max(next_id, int(id) + 1)
    print("Expense loaded from the file.")


def main_menu():
    load_expenses_from_file(DATA_FILE)
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Delete Expense")
        print("4. Summary of Expenses")
        print("5. Save Expense to File")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_Expense(date, amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)
        elif choice == '4':
            generate_summary()
        elif choice == '5':
            save_expenses_to_file(DATA_FILE)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid Option, Please try again.")


if __name__ == '__main__':
    main_menu()
