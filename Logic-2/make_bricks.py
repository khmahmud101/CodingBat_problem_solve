def make_bricks(small, big, goal):
    smalltotal = small * 1
    bigtotal = big * 5
    total = smalltotal + bigtotal
    if goal % 5 >= 0 and goal % 5 - small <= 0 and total >= goal:
        return True
    else:
        return False
