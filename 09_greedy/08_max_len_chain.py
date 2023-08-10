# https://leetcode.com/problems/maximum-length-of-pair-chain/
# Question : You are given n pairs of numbers. In every pair, the first number is always smaller
# than the second number. A pair (c, d) can follow another pair (a, b) if b < c.
# Chain of pairs can be formed in this fashion. Find the longest chain which can be formed
# from a given set of pairs.
# Similar : box stacking (20_initialFiles/file5), 01_array/04_longest_increasing_subsequnce
#
# Question Type : Generic
# Used : This can be easily solved as job selection problem described in
#        01_activity_selection.py in O(n log n).
#        Here, given two array start and finish.
#        Sort the finish array and accordingly sort the start array.
#        Make a MCL array with all values set as 1. Considering MCL[i] stores the maximum
#        chain length ending with pair i.
#        Run 2 loop outer : 1 to n-1 and inner : 0 to i.
#           Here we check if pair i can be suffixed to pair j and if MCL[i] < MCL[j] + 1.
#           Then update MCL[i] accordingly.
#        return max val from MCL array.
# Logic: maxChainLength(arr):
#        n = len(arr), MCL = [1] * n
#        for i in range(1, n):
#           for j in range(0, i):
#               if arr[i].a > arr[j].b and MCL[i] < MCL[j] + 1:
#                   MCL[i] = MCL[j] + 1
#        return max(MCL)
# Complexity : O(n^2)


class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


def maxChainLength(arr):
    n = len(arr)
    # max chain length
    MCL = [1] * n

    # This is used in longest increasing sub sequence in dynamic programming approach
    for i in range(1, n):
        for j in range(0, i):
            if arr[i].a > arr[j].b and MCL[i] < MCL[j] + 1:
                MCL[i] = MCL[j] + 1

    # MCL[i] now stores the maximum chain length ending with pair i
    return max(MCL)


if __name__ == "__main__":
    s = [5, 15, 27, 50]
    f = [24, 25, 40, 60]

    # s = [5, 15, 39, 50, 27]
    # f = [24, 28, 60, 90, 40]

    sortedStart = [x for _, x in sorted(zip(f, s))]
    sortedFinish = sorted(f)

    inpArr = []
    for i in range(len(sortedStart)):
        inpArr.append(Pair(sortedStart[i], sortedFinish[i]))

    print('Length of maximum size chain is:', maxChainLength(inpArr))
