# Question : Given an array of n integers where each value represents number of chocolates in a packet. Each packet
# can have variable number of chocolates. There are m students, the task is to distribute chocolate packets such that :
# Each student gets one packet.
# The difference between the number of chocolates in packet with maximum chocolates and packet with minimum chocolates
# given to the students is minimum.
#
# Question Type : Generic
# Used : sort the array, run a sliding window of size m and keep checking the minimum difference of each window
#        while i + m - 1 < n: diff = arr[i+m-1] - arr[i]
#           keep updating the minDiff
# Complexity : O(n log n)


def findMinDiff(arr, n, m):
    if m == 0 or n == 0:
        return 0
    arr.sort()
    if n < m:
        return -1
    minDiff = 99999
    first = 0
    last = 0
    i = 0
    while i + m - 1 < n:
        diff = arr[i+m-1] - arr[i]
        if diff < minDiff:
            minDiff = diff
            first = i
            last = i + m - 1
        i += 1
    return arr[last] - arr[first]


if __name__ == "__main__":
    arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
    m = 7
    print("Minimum difference:"),
    print(findMinDiff(arr, len(arr), m))
