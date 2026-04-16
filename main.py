import json
import matplotlib.pyplot as plt
expenses = []
def load_data():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except:
        expenses = []
def save_data():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    print("\n-Add Expense-")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Bills, etc): ")
    try:
        amount = float(input("Enter amount: "))
    except:
        print("Invalid amount!")
        return
    description = input("Enter description: ")
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    save_data()
    print("Expense added successfully!")

def view_expenses():
    print("\n-- All Expenses ---")
    if not expenses:
        print("No expenses found.")
        return

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['description']}")

def monthly_summary():
    print("\n--- Monthly Summary ---")
    month = input("Enter month (YYYY-MM): ")

    total = 0
    for exp in expenses:
        if exp["date"].startswith(month):
            total += exp["amount"]

    print(f"Total spending in {month}: ₹{total}")

def category_breakdown():
    print("\n--- Category Breakdown ---")

    if not expenses:
        print("No data available.")
        return

    category_totals = {}

    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    for cat, amt in category_totals.items():
        print(f"{cat}: ₹{amt}")

def highest_category():
    print("\n--- Highest Spending Category ---")

    if not expenses:
        print("No data available.")
        return

    category_totals = {}

    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    highest = max(category_totals, key=category_totals.get)
    print(f"Highest spending is in '{highest}' → ₹{category_totals[highest]}")

def show_pie_chart():
    print("\n--- Expense Pie Chart ---")

    if not expenses:
        print("No data to display.")
        return

    category_totals = {}

    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    labels = list(category_totals.keys())
    values = list(category_totals.values())

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()

def main():
    load_data()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Breakdown")
        print("5. Highest Spending Category")
        print("6. Show Pie Chart")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            monthly_summary()
        elif choice=="4":
            category_breakdown()
        elif choice=="5":
            highest_category()
        elif choice=="6":
            show_pie_chart()
        elif choice=="7":
            print("Goodbye")
            break
        else:
            print("Invalid choice.Try again.")

main()
