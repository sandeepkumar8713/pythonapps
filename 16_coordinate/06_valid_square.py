# https://leetcode.com/problems/valid-square/
# Question : Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the
# four points construct a square. The coordinate of a point pi is represented as [xi, yi].
# The input is not given in any order. A valid square has four equal sides with positive
# length and four equal angles (90-degree angles).
#
# Example : Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true
#
# Question Type : Generic
# Used : Find all 4 possible side distance and 2 diagonals.
#        Sort the distance array.
#        Check top 4 values of sorted array for side equality.
#        Check bottom 2 values for diagonal equality.
#        Logic:
#        d12 = distance(p1, p2), d13 = distance(p1, p3)
#        d14 = distance(p1, p4), d23 = distance(p2, p3)
#        d24 = distance(p2, p4), d34 = distance(p3, p4)
#        arr = [d12, d13, d14, d23, d24, d34]
#        arr.sort()
#        if 0 not in arr and arr[0] == arr[1] == arr[2] == arr[3] and arr[4] == arr[5]:
#           return True
#        return False
# Complexity : O(1)


def distance(a, b):
    return (b[1] - a[1]) ** 2 + (b[0] - a[0]) ** 2


def validSquare(p1, p2, p3, p4):
    d12 = distance(p1, p2)
    d13 = distance(p1, p3)
    d14 = distance(p1, p4)
    d23 = distance(p2, p3)
    d24 = distance(p2, p4)
    d34 = distance(p3, p4)
    arr = [d12, d13, d14, d23, d24, d34]
    arr.sort()
    # check sides and diagonal
    if 0 not in arr and arr[0] == arr[1] == arr[2] == arr[3] and arr[4] == arr[5]:
        return True
    return False


if __name__ == "__main__":
    p1 = [0, 0]
    p2 = [1, 1]
    p3 = [1, 0]
    p4 = [0, 1]
    print(validSquare(p1, p2, p3, p4))

    p1 = [0, 0]
    p2 = [1, 1]
    p3 = [1, 0]
    p4 = [0, 12]
    print(validSquare(p1, p2, p3, p4))
