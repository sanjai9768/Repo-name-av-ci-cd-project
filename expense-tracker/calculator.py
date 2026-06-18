def total_expense(expenses):
    total = 0
    for e in expenses:
        total += e["amount"]
    return total

def check_limit(total, limit):
    if total > limit:
        return "Limit Exceeded"
    return "Within Limit"