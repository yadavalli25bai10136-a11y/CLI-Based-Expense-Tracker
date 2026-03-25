from datetime import datetime
from storage import load_data, save_data

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    
    expense = {
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    data = load_data()
    data.append(expense)
    save_data(data)

    print("Expense added successfully!")

def view_expenses():
    data = load_data()

    if not data:
        print("No expenses found.")
        return

    for i, exp in enumerate(data, 1):
        print(f"{i}. {exp['amount']} | {exp['category']} | {exp['date']}")

def show_summary():
    data = load_data()

    summary = {}

    for exp in data:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    print("\nCategory-wise Summary:")
    for cat, total in summary.items():
        print(f"{cat}: {total}")
