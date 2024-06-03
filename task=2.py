class BudgetTracker:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.balance -= amount

    def display_balance(self):
        print(f"Current balance: ${self.balance}")

    def display_expenses(self):
        if self.expenses:
            print("Expenses:")
            for category, amount in self.expenses.items():
                print(f"{category}: ${amount}")
        else:
            print("No expenses recorded yet.")

# Creating a budget tracker with an initial balance of $1000
my_budget = BudgetTracker(1000)

# Adding expenses
my_budget.add_expense("Food", 50)
my_budget.add_expense("Transportation", 30)
my_budget.add_expense("Entertainment", 100)

# Displaying balance and expenses
my_budget.display_balance()
my_budget.display_expenses()