class Expense:
    def __init__(self, category, amount, description):
        self.category = category
        self.amount = amount
        self.description = description

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, description):
        expense = Expense(category, amount, description)
        self.expenses.append(expense)

    def get_total_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total

    def get_expenses_by_category(self, category):
        expenses_by_category = []
        for expense in self.expenses:
            if expense.category.lower() == category.lower():
                expenses_by_category.append(expense)
        return expenses_by_category

def main():
    tracker = ExpenseTracker()

    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            tracker.add_expense(category, amount, description)
            print("Expense added successfully!")
        elif choice == "2":
            total_expenses = tracker.get_total_expenses()
            print(f"Total expenses: ${total_expenses}")
        elif choice == "3":
            category = input("Enter expense category to filter: ")
            expenses_by_category = tracker.get_expenses_by_category(category)
            print(f"Expenses in category '{category}':")
            for expense in expenses_by_category:
                print(f"- Amount: ${expense.amount}, Description: {expense.description}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
