from expense import add_expense, get_all_expenses

def test_add_expense():
    add_expense("food", 100)
    data = get_all_expenses()
    assert len(data) > 0