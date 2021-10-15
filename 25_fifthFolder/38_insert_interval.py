# https://leetcode.com/problems/insert-interval/
# Similar : 24_fourthFolder/11_merge_overlapping_intervals
# Question : You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the ith interval and
# intervals is sorted in ascending order by starti. You are also given an interval
# newInterval = [start, end] that represents the start and end of another interval. Insert
# newInterval into intervals such that intervals is still sorted in ascending order by starti
# and intervals still does not have any overlapping intervals (merge overlapping intervals
# if necessary). Return intervals after the insertion.
#
# Example : Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
# Question Type : Generic
# Used : Do 2 binary search, to find start and end of newInterval in given intervals.
#        let the result be index startI and endI
#        res will be [0:startI]
#        if endI < len(interval):
#           if newEnd < interval[endI][0]:
#               append newinterval with newEnd and remaining interval after endI to res
#           else:
#               append newinterval with existing end and remaining interval after endI + 1 to res
#        else:
#           append newinterval to res
#        return res
# Complexity : O(log n)


def bin_search(intervals, target):
    i, j = 0, len(intervals) - 1
    if target > intervals[-1][1]:
        return j + 1
    if target <= intervals[0][1]:
        return 0
    while i < j:
        k = (i + j) // 2
        if intervals[k][1] == target:
            return k
        elif intervals[k][1] < target:
            i = k + 1
        else:
            j = k
    return i


def insert(intervals, newInterval):
    if len(intervals) == 0:
        return [newInterval]
    if newInterval[1] < intervals[0][0]:
        return [newInterval] + intervals
    if newInterval[0] > intervals[-1][-1]:
        return intervals + [newInterval]

    newStart = newInterval[0]
    newEnd = newInterval[1]

    startI = bin_search(intervals, newStart)
    endI = bin_search(intervals, newEnd)
    res = intervals[:startI]
    if endI < len(intervals):
        # new interval will start and end within present interval
        if newEnd < intervals[endI][0]:
            new_interval = [min(newStart, intervals[startI][0]), newEnd]
            res += [new_interval]
            res += intervals[endI:]
        else:
            new_interval = [min(newStart, intervals[startI][0]), intervals[endI][1]]
            res += [new_interval]
            res += intervals[endI + 1:]
    else:
        # new interval will end after the present interval
        new_interval = [min(newStart, intervals[startI][0]), newEnd]
        res += [new_interval]

    return res


if __name__ == "__main__":
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print (insert(intervals, newInterval))
