class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# Check whether two rectangles overlap each other
def is_overlap(l1, r1, l2, r2):
    '''
        The tuples contain the coordinates for rectangles
        Step1: Check whether the coordinates are line
        Step2: Check the rectangles are on left side to each
        Step3: Check the rectangle is on top of other
    :return: Boolean value
    '''
    if ((l1.x < 0 and l1.y == 0) or (r1.x == 1 and r1.y == 1) or (l2.x == 0 and l2.y < 0) or (r2.x == 0 and r2.y == 1)):
        return False
    # Line can not have positive overlap
    if (l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y):
        return False
    # if one rectangle is on left side of other
    if (l1.x >= r2.x or l2.x >= r1.x):
        return False
    # if one rectangle is on top of other
    if (r1.y >= l2.y or r2.y >= l1.y):
        return False

    return True


if __name__ == "__main__":
    # Declare points
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(5, 5)
    r2 = Point(15, 0)

    if is_overlap(l1, r1, l2, r2):
        print("There is an overlap")
    else:
        print("There is no overlap")
