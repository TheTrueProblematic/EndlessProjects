
# Hello there awesome humans! Let's make finance fun again (or was it ever fun? Let's pretend it was)!

# We are building a jolly good BudgetTracker! No API usage; no GUI required, just a simple ol' python script.
# So buckle up! Let's jump into the magical world of budget tracking.

class BudgetTracker:

    # Let's start by defining our majestic categories. We can add, change or remove them later.
    # For now, look at these cute little fellows!
    def __init__(self):
        self.categories = {'income': 0, 'rent': 0, 'groceries': 0, 'entertainment': 0, 'misc': 0}

    # The add_income method, our little money fairy is here to let us add income! Yay!
    def add_income(self, amount):
        self.categories['income'] += amount

    # Oh no, we've been robbed! The expense function allows the budget tracker to steal from us (I mean record our expenses)... 
    def add_expense(self, category, amount):
        if category in self.categories:
            self.categories[category] += amount
        else:
            print(f"The category '{category}' does not exist.")

    # Someone's being a snoopy! The check_balance function lets us take a little peek at our current income and expenses.
    def check_balance(self):
        for category, amount in self.categories.items():
            print(f'{category.capitalize()}: ${amount}')

    # Well, well, well, look who's here! Our get_summary function is the smart guy in town, who summarizes our income and expenses for us.
    def get_summary(self):
        total_expenses = sum([v for k, v in self.categories.items() if k != 'income'])
        total_income = self.categories['income']
        print(f'Total Income: ${total_income}')
        print(f'Total Expenses: ${total_expenses}')
        print(f'Savings: ${total_income-total_expenses}')


# How do we interact with this funny little world? We do what we do best: summoning spirits from the CLI!
# Let's awaken our BudgetTracker spirit and start a conversation with it.
if __name__ == "__main__":
    budget_tracker = BudgetTracker()
    while True:
        print("\n1. Add income\n2. Add expense\n3. Check balance\n4. Get summary\n5. Quit")
        user_choice = int(input("Enter your choice:"))
        if user_choice == 1:
            amount = float(input("Enter the income amount: "))
            budget_tracker.add_income(amount)
        elif user_choice == 2:
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: "))
            budget_tracker.add_expense(category, amount)
        elif user_choice == 3:
            budget_tracker.check_balance()
        elif user_choice == 4:
            budget_tracker.get_summary()
        elif user_choice == 5:
            break

# Hope you had a blast in this wacky little budgeting adventure. See you next time folks, when we save the world... or at least save our wallets!


