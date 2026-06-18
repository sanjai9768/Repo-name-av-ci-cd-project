expenses = []

def add_expense(category, amount):
    expenses.append({"category": category, "amount": amount})

def get_all_expenses():
    return expenses