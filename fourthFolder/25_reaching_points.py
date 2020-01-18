# https://github.com/yuanhui-yang/LeetCode/blob/master/Algorithms/reaching-points.cpp
# Question : A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
# Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of
# moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.
#
# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation: One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#
# Used : Run a loop to reduce target to source.
#           If sx == tx is same, return true if y's difference is divisible by sx
#           If sy == ty is same, return true if x's difference is divisible by sy
#           If tx < ty : ty = ty % tx else tx = tx % ty
#        return true if target is equal to source.
# Complexity : O(n)


def reachingPoints(sx, sy, tx, ty):
    while tx >= sx and ty >= sy and tx != ty:
        if tx == sx:
            return (ty - sy) % sx == 0

        if ty == sy:
            return (tx - sx) % sy == 0

        if tx < ty:
            ty %= tx
        else:
            tx %= ty

    return tx == sx and ty == sy


if __name__ == "__main__":
    sx = 1
    sy = 1
    tx = 3
    ty = 5
    print reachingPoints(sx, sy, tx, ty)
