import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Connecting to SQLite database
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Creating the expenses table
cursor.execute('''
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    date TEXT,
    amount REAL,
    category TEXT
)
''')

conn.commit()

# Add a new expense
def add_expense(date, amount, category):
    try:
        pd.to_datetime(date, format='%d-%m-%Y')  # Validates date format
        cursor.execute('''
        INSERT INTO expenses (date, amount, category)
        VALUES (?, ?, ?)
        ''', (date, amount, category))
        conn.commit()
        print("Expense added successfully!")
    except ValueError:
        print("Invalid date format. Use DD-MM-YYYY.")
    except Exception as e:
        print(f"Error: {e}")

# Show all expenses
def get_expenses():
    cursor.execute('SELECT * FROM expenses')
    return cursor.fetchall()

# Show remaining budget
def calculate_remaining_budget(monthly_budget):
    cursor.execute('SELECT SUM(amount) FROM expenses')
    total_spent = cursor.fetchone()[0]
    if total_spent is None:
        total_spent = 0
    return monthly_budget - total_spent

# Check for budget alert
def check_budget_alert(monthly_budget):
    remaining_budget = calculate_remaining_budget(monthly_budget)
    if remaining_budget < 0:
        print("Warning: You have exceeded your monthly budget!")

# Plot pie chart
def plot_expenses():
    cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    data = cursor.fetchall()
    if data:
        df = pd.DataFrame(data, columns=['Category', 'Amount'])
        plt.figure(figsize=(8, 8))
        plt.pie(df['Amount'], labels=df['Category'], autopct='%1.1f%%', startangle=140)
        plt.title('Expenses by Category')
        plt.show()
    else:
        print("No expenses to plot.")

# Remove all expenses
def remove_all_expenses():
    confirmation = input("Are you sure? (y/n): ")
    if confirmation == 'y':
        cursor.execute('DELETE FROM expenses')
        conn.commit()
        print("All records deleted successfully!")
    else:
        print("Operation cancelled.")

# Export expenses to CSV
def export_data_to_csv():
    expenses = get_expenses()
    if expenses:
        df = pd.DataFrame(expenses, columns=['ID', 'Date', 'Amount', 'Category'])
        df.to_csv('expenses_backup.csv', index=False)
        print("Data exported to 'expenses_backup.csv'.")
    else:
        print("No data to export.")

# Import expenses from CSV
def import_data_from_csv():
    try:
        df = pd.read_csv('expenses_backup.csv')
        for _, row in df.iterrows():
            add_expense(row['Date'], row['Amount'], row['Category'])
        print("Data imported successfully.")
    except Exception as e:
        print(f"Error during import: {e}")

# Monthly expense report
def monthly_expense_report():
    cursor.execute('''
    SELECT strftime('%m-%Y', date) as month, SUM(amount)
    FROM expenses GROUP BY month
    ''')
    report = cursor.fetchall()
    for row in report:
        print(f"Month: {row[0]}, Total Expense: {row[1]}")

# Select category from predefined list
def select_category():
    categories = ['Food', 'Transport', 'Shopping', 'Rent', 'Utilities', 'Others']
    print("Select a category:")
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")
    choice = int(input("Enter your choice: "))
    return categories[choice - 1]

# Change monthly budget
def change_monthly_budget():
    global monthly_budget
    new_budget = float(input("Enter new monthly budget: "))
    monthly_budget = new_budget
    print(f"Monthly budget changed to {monthly_budget}.")

# Display menu
def menu():
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Remaining Budget")
    print("4. Plot Expenses")
    print("5. Remove All Expenses")
    print("6. Export Expenses to CSV")
    print("7. Import Expenses from CSV")
    print("8. Monthly Expense Report")
    print("9. Exit")

# Authenticate user
def authenticate():
    password = "mypassword"
    attempts = 3
    while attempts > 0:
        user_input = input("Enter Password: ")
        if user_input == password:
            print("Access Granted.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts left.")
    print("Access Denied.")
    return False

# Main function
def main():
    global monthly_budget
    monthly_budget = 10000  # Default budget
    if authenticate():
        while True:
            menu()  # Display the menu
            choice = int(input("Enter your choice: "))
            if choice == 1:
                date = input("Enter date (DD-MM-YYYY): ")
                amount = float(input("Enter amount: "))
                category = select_category()
                add_expense(date, amount, category)
            elif choice == 2:
                expenses = get_expenses()
                if expenses:
                    for expense in expenses:
                        print(expense)
                else:
                    print("No expenses to view.")
            elif choice == 3:
                remaining_budget = calculate_remaining_budget(monthly_budget)
                print(f"Remaining Budget: {remaining_budget}")
                check_budget_alert(monthly_budget)  # Alert check
            elif choice == 4:
                plot_expenses()
            elif choice == 5:
                remove_all_expenses()
            elif choice == 6:
                export_data_to_csv()
            elif choice == 7:
                import_data_from_csv()
            elif choice == 8:
                monthly_expense_report()
            elif choice == 9:
                break
            else:
                print("Invalid choice! Please try again.")
        conn.close()

if __name__ == "__main__":
    main()
