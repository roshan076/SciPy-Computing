# Expense Tracker

This project demonstrates how to use **Lambda Functions** in Python to build an **Expense Tracker**. The application allows users to add expenses, list all expenses, calculate total expenses, and filter expenses by category.

---

## Features

- **Add Expense**: Allows the user to input an amount and category for each expense, which is then stored in the expenses list.
- **List Expenses**: Displays all recorded expenses, showing the amount and category.
- **Total Expenses**: Calculates the total sum of all expenses.
- **Filter by Category**: Filters and displays expenses based on a specific category.
- **Looped Interaction**: The user is given multiple choices in a loop until they decide to exit the program.

---

## How It Works

The Expense Tracker utilizes the following Python concepts:
- **Lambda Functions**: Used to filter and sum expenses based on certain criteria (e.g., category or amount).
- **Higher-Order Functions**: Functions like `map()` and `filter()` are used to process the expense list.
- **User Input**: Users interact with the program through a simple text-based interface.

### Core Functions:

- **`add_expense(expenses, amount, category)`**: Adds a new expense to the list.
- **`print_expenses(expenses)`**: Prints all expenses in a readable format.
- **`total_expenses(expenses)`**: Calculates and returns the total sum of all expenses.
- **`filter_expenses_by_category(expenses, category)`**: Filters expenses based on the given category.
