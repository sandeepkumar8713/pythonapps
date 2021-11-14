# CTCI : Q17_05_Letters_and_Numbers
# Question : Given an array containing only 0s and 1s, find the largest sub array which contain
# equal no of 0s and 1s.
# Expected time complexity is O(n).
#
# Input: arr[] = {1, 0, 1, 1, 1, 0, 0}
# Output: 1 to 6 (Starting and Ending indexes of output sub array)
#
# Question Type : Generic
# Used : Convert all 0 to -1
#        Keep updating sum in hash dict
#        if the running sum is already in hash dict, get the diff b/w the two index.
#        Logic :
#        for i in range(len(arr)):
#           arrSum += arr[i]
#           if arrSum == 0:
#               maxLen = i+1, endIndex = i
#           if arrSum + n in hmap:
#               if maxLen < (i - hmap[arrSum + n]):
#                   maxLen = i - hmap[arrSum + n]
#                   endIndex = i
#           else:
#               hmap[arrSum+n] = i
# Complexity : O(n)


def maxLen(arr):
    n = len(arr)
    hmap = dict()
    maxLen = 0
    endIndex = -1
    arrSum = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1

    for i in range(len(arr)):
        arrSum += arr[i]

        if arrSum == 0:
            maxLen = i+1
            endIndex = i

        if arrSum + n in hmap:
            if maxLen < (i - hmap[arrSum + n]):
                maxLen = i - hmap[arrSum + n]
                endIndex = i
        else:
            hmap[arrSum+n] = i

    for i in range(len(arr)):
        if arr[i] == -1:
            arr[i] = 0

    if maxLen == 0:
        return -1, -1

    return endIndex-maxLen+1, endIndex


if __name__ == "__main__":
    # arr = [1, 1, 1, 1]
    arr = [1, 0, 0, 1, 0, 1, 1]
    print (maxLen(arr))
