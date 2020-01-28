# http://buttercola.blogspot.com/2016/06/leetcode-321-create-maximum-number.html
# Question : Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number
# of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved.
# Return an array of the k digits. You should try to optimize your time and space complexity.
#
# Example:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# return [9, 8, 6, 5, 3]
#
# Question Type : ShouldSee
# Used : First find out the maximum number for each array, and then merge it into a global maximal one.
#        Run a loop from i : 0 to k
#           choose max elements from array1 of size i and from array2 of size k - i
#           Now merge these amx arrays
#           Update maxArray found till now
#         Logic:
#         def maxNumber(inpArr1, inpArr2, k):
#           i = max(k - len2, 0)
#           limit = min(len1, k)
#           while i <= limit:
#               list1 = findMax(inpArr1, i)
#               list2 = findMax(inpArr2, k - i)
#               curr = merge(list1, list2)
#               if greater(curr, 0, resList, 0): resList = curr
#               i += 1
#           return resList
#         def findMax(inpArr, k):
#           length = 0
#           for i in range(n):
#               while length > 0 and length + n - i > k and inpArr[i] > result[length-1]:
#                   length -= 1
#               if length < k:
#               result[length] = inpArr[i]
#               length += 1
#           return result
# Complexity : O(n^3)


def merge(inpArr1, inpArr2):
    n1 = len(inpArr1)
    n2 = len(inpArr2)
    result = [0] * (n1+n2)

    i = j = k = 0
    while k < n1 + n2:
        if greater(inpArr1, i, inpArr2, j):
            result[k] = inpArr1[i]
            i += 1
        else:
            result[k] = inpArr2[j]
            j += 1
        k += 1

    return result


def greater(inpArr1, pos1, inpArr2, pos2):
    n1 = len(inpArr1)
    n2 = len(inpArr2)
    while pos1 < n1 and pos2 < n2 and inpArr1[pos1] == inpArr2[pos2]:
        pos1 += 1
        pos2 += 1
    if pos2 == n2:
        return True
    if pos1 < n1 and inpArr1[pos1] > inpArr2[pos2]:
        return True
    return False


def findMax(inpArr, k):
    result = [0] * k
    n = len(inpArr)
    length = 0
    for i in range(n):
        while length > 0 and length + n - i > k and inpArr[i] > result[length-1]:
            length -= 1

        if length < k:
            result[length] = inpArr[i]
            length += 1

    print(result)
    return result


def maxNumber(inpArr1, inpArr2, k):
    resList = [0] * k
    len1 = len(inpArr1)
    len2 = len(inpArr2)
    i = max(k - len2, 0)
    limit = min(len1, k)
    while i <= limit:
        list1 = findMax(inpArr1, i)
        list2 = findMax(inpArr2, k - i)

        curr = merge(list1, list2)

        if greater(curr, 0, resList, 0):
            resList = curr

        i += 1
    return resList


if __name__ == "__main__":
    inpArr1 = [3, 4, 6, 5]
    inpArr2 = [9, 1, 2, 5, 8, 3]

    #inpArr1 = [6, 7]
    #inpArr2 = [6, 0, 4]
    print(maxNumber(inpArr1, inpArr2, 5))
