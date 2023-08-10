# https://leetcode.com/problems/non-overlapping-intervals/
# Question : Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of the
# intervals non-overlapping.
#
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
#
# Question Type : Generic
# Used : Sort the given intervals based on second element.
#        Loop over the intervals.
#        For each interval at index i, the code checks if the end point of the previous interval (at index prev)
#        is greater than the start point of the current interval (at index i). If this condition is true,
#        it means there is an overlap between the two intervals.
#        Otherwise, if there is no overlap, the prev variable is updated to i. This indicates that the current
#        interval will be considered as the next non-overlapping interval.
# Logic: intervals.sort(key=lambda x: x[1])
#        prev = 0, count = 0
#        for i in range(1, len(intervals)):
#           if intervals[prev][1] > intervals[i][0]:
#               count += 1
#           else:
#               prev = i
#        return count
# Complexity : O(n log n)

def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    prev = 0
    count = 0

    for i in range(1, len(intervals)):
        if intervals[prev][1] > intervals[i][0]:
            count += 1
        else:
            prev = i

    return count


if __name__ == "__main__":
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(eraseOverlapIntervals(intervals))

    intervals = [[1, 2], [1, 2], [1, 2]]
    print(eraseOverlapIntervals(intervals))
