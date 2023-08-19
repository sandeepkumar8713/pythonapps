# https://leetcode.com/problems/merge-intervals/
# Question : Given a set of time intervals in any order, merge all overlapping intervals
# into one and output the result which should have only mutually exclusive intervals.
# Let the intervals be represented as pairs of integers for simplicity.
# For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8}}. The
# intervals {1,3} and {2,4} overlap with each other, so they should be merged and
# become {1, 4}. Similarly {5, 7} and {6, 8} should be merged and become {5, 8}
#
# Question Type : Generic
# Used : Make a class Interval of field start and end. Make a sorted list of intervals
#        based on start time.
#        Loop over sorted list, if start of index-1 is less than end of index,
#        then merge it by setting max and min of start and end.
#        for i in range(len(sortedL)):
#           if index != 0 and sortedL[i].start <= sortedL[index-1].end:
#               while index != 0 and sortedL[i].start <= sortedL[index-1].end:
#                   sortedL[index - 1].end = max(sortedL[index - 1].end, sortedL[i].end)
#                   sortedL[index - 1].start = min(sortedL[index - 1].start, sortedL[i].start)
#                   index -= 1
#           else:
#               sortedL[index] = sortedL[i]
#           index += 1
# Complexity : O(n log n)

import functools


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def compare(A, B):
    if A.start == B.start:
        return 0
    elif A.start < B.start:
        return -1
    else:
        return 1


def mergeIntervals(intervalList):
    sortedL = sorted(intervalList, key=functools.cmp_to_key(compare))
    index = 0

    for i in range(len(sortedL)):
        print(sortedL[i].start, sortedL[i].end)

    for i in range(len(sortedL)):
        if index != 0 and sortedL[i].start <= sortedL[index-1].end:
            while index != 0 and sortedL[i].start <= sortedL[index-1].end:
                sortedL[index - 1].end = max(sortedL[index - 1].end, sortedL[i].end)
                sortedL[index - 1].start = min(sortedL[index - 1].start, sortedL[i].start)
                index -= 1
        else:
            sortedL[index] = sortedL[i]
        index += 1

    print("result : ")
    for i in range(index):
        print(sortedL[i].start, sortedL[i].end)


if __name__ == "__main__":
    #inpArr = [[6, 8], [1, 9], [2, 4], [4, 7]]
    inpArr = [[1, 3], [2, 4], [5, 7], [6, 8]]
    intervalList = []
    for i in range(len(inpArr)):
        intervalList.append(Interval(inpArr[i][0], inpArr[i][1]))
    mergeIntervals(intervalList)
