# CTCI : Q16_03_Intersection
# https://www.geeksforgeeks.org/program-for-point-of-intersection-of-two-lines/
# Question :  Given points A and B corresponding to line AB and points P and Q corresponding to line PQ, find the
# point of intersection of these lines. The points are given in 2D Plane with their X and Y Coordinates.
#
# Question Type : ShouldSee
# Used : a1 = B.y - A.y; b1 = A.x - B.x
#        c1 = a1*A.x + b1*A.y
#        determinant = float(a1*b2 - a2*b1)
#        if determinant == 0: print ("Given lines are parallel")
#        else: x = (b2*c1 - b1*c2) / determinant; y = (a1*c2 - a2*c1) / determinant
# Complexity : O(1)


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


def lineIntersection(A, B, C, D):
    # Line AB represented as a1x + b1y = c1
    a1 = B.y - A.y
    b1 = A.x - B.x
    c1 = a1*A.x + b1*A.y

    # Line CD represented as a2x + b2y = c2
    a2 = D.y - C.y
    b2 = C.x - D.x
    c2 = a2*C.x + b2*C.y

    determinant = float(a1*b2 - a2*b1)

    if determinant == 0:
        print ("Given lines are parallel")
    else:
        x = (b2*c1 - b1*c2) / determinant
        y = (a1*c2 - a2*c1) / determinant
        print (x, y)


if __name__ == "__main__":
    A = Point(1, 1)
    B = Point(4, 4)

    #C = Point(2, 2)
    #D = Point(8, 8)

    C = Point(1, 8)
    D = Point(2, 4)

    lineIntersection(A, B, C, D)
