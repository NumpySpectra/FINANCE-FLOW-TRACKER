# Personal Expense Tracker

This Python-based Personal Expense Tracker application is designed to help users manage their finances effectively. It enables users to log, categorize, analyze, and visualize their expenses while staying within a monthly budget.

## Features

- **Authentication**: Secure access with a password system.
- **Set Monthly Budget**: Define and adjust your monthly budget.
- **Add Expense**: Log your expenses by date, amount, and category.
- **View Expenses**: Display all recorded expenses.
- **Remaining Budget**: Calculate and display the remaining budget.
- **Budget Alert**: Alerts you if the budget is exceeded.
- **Plot Expenses**: Visualize your spending with a pie chart categorized by expense type.
- **Monthly Expense Report**: View a summary of monthly expenses.
- **Export to CSV**: Backup expense data to a CSV file.
- **Import from CSV**: Restore expenses from a CSV file.
- **Remove All Expenses**: Clear all recorded expenses.
- **Predefined Categories**: Simplifies categorization with preset options like Food, Transport, Shopping, etc.

## Technologies Used

- **Python**: Core programming language for application development.
- **SQLite**: For managing the lightweight and portable expense database.
- **pandas**: Facilitates data analysis and CSV file operations.
- **matplotlib**: Generates pie charts to visualize expense distribution.



## Usage

1. Run the program:
   bash
   python expense_tracker.py
   
2. Authenticate with the password (`mypassword` by default).
3. Choose options from the menu to manage your expenses.

## Menu Options

1. **Add Expense**: Input the date, amount, and category of an expense.
2. **View All Expenses**: Displays all logged expenses.
3. **View Remaining Budget**: Shows remaining budget after accounting for expenses.
4. **Plot Expenses**: Displays a pie chart of expenses by category.
5. **Remove All Expenses**: Deletes all recorded expenses (confirmation required).
6. **Export Expenses to CSV**: Saves expenses to `expenses_backup.csv`.
7. **Import Expenses from CSV**: Restores expenses from `expenses_backup.csv`.
8. **Monthly Expense Report**: Displays total expenses grouped by month.
9. **Exit**: Closes the application.

## Database Schema

The application uses an SQLite database with the following schema:

| Column    | Type    | Description                   |
|-----------|---------|-------------------------------|
| id        | INTEGER | Unique identifier for expenses|
| date      | TEXT    | Date of the expense (DD-MM-YYYY)|
| amount    | REAL    | Amount spent                 |
| category  | TEXT    | Category of the expense      |

