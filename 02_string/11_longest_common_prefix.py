# Question : Given a set of strings, find the longest common prefix.
#
# Input  : {"geeksforgeeks", "geeks", "geek", "geezer"}
# Output : "gee"
#
# Used : find the string with minimum length
#        Do binary search over it. First check if left to mid is present in all the strings in array. If yes and add to
#        prefix. If not, then make right as mid -1
#        Once left half is matched, then it move to right half with left = mid + 1, and repeat the above process
# Complexity : O(NM log M) where M is length of shortest string


def findMinLen(arr):
    minLen = 99999
    for item in arr:
        if minLen > len(item):
            minLen = len(item)
    return minLen


def allContainsPrefix(arr, matchStr, start, end):
    for arrStr in arr:
        for i in range(start, end+1):
            if arrStr[i] != matchStr[i]:
                return False
    return True


def commanPrefix(arr):
    minLen = findMinLen(arr)
    prefix = ''
    low = 0
    high = minLen

    while low <= high:
        mid = low + (high - low)/2
        if allContainsPrefix(arr, arr[0], low, mid):
            prefix += arr[0][low:mid+1]
            low = mid + 1
        else:
            high = mid - 1

    return prefix


if __name__ == "__main__":
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    #arr = ["apple", "ape", "april"]
    print commanPrefix(arr)
