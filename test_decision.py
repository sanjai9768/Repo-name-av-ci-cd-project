from decision import decide_action

def test_stop():
    assert decide_action(10) == "STOP"

def test_move():
    assert decide_action(30) == "MOVE"