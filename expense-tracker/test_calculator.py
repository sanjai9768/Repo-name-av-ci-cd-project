from calculator import total_expense, check_limit

def test_total():
    expenses = [{"category": "food", "amount": 100}]
    assert total_expense(expenses) == 100

def test_limit():
    assert check_limit(1200, 1000) == "Limit Exceeded"