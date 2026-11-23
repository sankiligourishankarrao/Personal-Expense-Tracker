# Personal Expense Tracker

A menu-driven command-line program in Python for recording daily expenses and seeing where the money goes.

## Features

- **Add** an expense with date, amount, category, and description
- **View** all expenses, or filter by date or by category (case-insensitive)
- **Delete** an expense by its ID
- **Summary** of total spending per category
- **Save and load** expenses to a text file (`expenses.txt`), so data survives between runs

## Run it

Needs Python 3, no extra packages.

```bash
python3 expense_tracker.py
```

## Example session

```text
Personal Expense Tracker
1. Add Expense
2. View Expense
3. Delete Expense
4. Summary of Expenses
5. Save Expense to File
6. Exit
Choose an option: 4
Category: Food, Total Amount: 245.0.
Category: Study, Total Amount: 130.0.
```

## How it works

- Expenses are stored in a list of dictionaries (`id`, `date`, `amount`, `category`, `description`), with an auto-incrementing ID.
- Filtering uses list comprehensions; the summary groups amounts by category with a dictionary.
- Saving writes one comma-separated line per expense; loading parses each line back and continues the ID counter.

## History

Built in Google Colab in October 2024. The original notebook printout is in [minor project.pdf](minor%20project.pdf). `expense_tracker.py` is the same program as a runnable script, with two fixes: it starts cleanly when `expenses.txt` doesn't exist yet, and it trims spaces when loading saved data.
