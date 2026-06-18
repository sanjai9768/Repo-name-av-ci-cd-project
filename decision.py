def decide_action(distance):
    if distance < 15:
        return "STOP"
    return "MOVE"