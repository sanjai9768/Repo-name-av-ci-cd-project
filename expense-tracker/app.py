from expense import add_expense, get_all_expenses
from calculator import total_expense, check_limit

add_expense("food", 200)
add_expense("travel", 150)
add_expense("shopping", 500)

expenses = get_all_expenses()

print("All Expenses:", expenses)
print("Total:", total_expense(expenses))

print(check_limit(total_expense(expenses), 1000))