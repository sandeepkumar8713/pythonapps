# https://www.geeksforgeeks.org/find-minimum-moves-reach-target-infinite-line/
# https://www.geeksforgeeks.org/minimum-steps-to-reach-a-destination/
# Question : Given a number line from -infinity to +infinity. You start at 0 and can go either
# to the left or to the right. The condition is that in i'th move, you take i steps.
# a) Find if you can reach a given number x
# b) Find the most optimal way to reach a given number x, if we can indeed reach it.
# For example, 3 can be reached in
# 2 steps, (0, 1) (1, 3) and 4 can be reached in 3 steps (0, -1), (-1, 1) (1, 4).
#
# Question Type : Generic
# Used : Call a recursive function steps(source, step, dest) with input steps(0, 0, dest)
#        if abs(source) > dest: return sys.maxsize
#        if source == dest: return step
#        From here we can either go right or left:
#        pos = steps(source + step + 1, step + 1, dest)
#        neg = steps(source - step - 1, step + 1, dest)
#        return min(pos, neg)
# Complexity : O(2^n)

import sys


def steps(source, step, dest):
    if abs(source) > dest:
        return sys.maxsize

    if source == dest:
        return step

    # at each point we can go either way
    pos = steps(source + step + 1, step + 1, dest)

    # if we go on negative side
    neg = steps(source - step - 1, step + 1, dest)

    return min(pos, neg)


if __name__ == "__main__":
    dest = 11
    print("No. of steps required to reach ", dest, " is ", steps(0, 0, dest))

