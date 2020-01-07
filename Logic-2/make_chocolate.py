def make_chocolate(small, big, goal):
    bigbar = 5 * big

    if goal >= bigbar:
        remainder = goal - bigbar
    else:
        remainder = goal % 5

    if remainder <= small:
        return remainder
    return -1
