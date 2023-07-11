# https://www.geeksforgeeks.org/find-top-k-or-most-frequent-numbers-in-a-stream/
# https://leetcode.com/problems/top-k-frequent-elements/
# Question : Given an array of n numbers. Your task is to read numbers from the array and
# keep at-most K numbers at the top (According to their decreasing frequency) every time a
# new number is read. We basically need to print top k numbers sorted by frequency when
# input stream has included k distinct elements, else need to print all distinct elements
# sorted by frequency.
#
# Question Type : ShouldSee
# Used : Make a list topElements of size k+1. set lastIndex=0. It is a marker that tells
#        up to which index data is filled in topElements. Maintain a dict freqMap which
#        stores frequency of each distinct element.
# Logic: kTop(arr, n, k):
#        for i in range(n):
#           Update the freqMap for this element.
#           If ele is not present in topElements:
#               topElements[lastIndex] = ele, set j = lastIndex
#               If lastIndex < k: lastIndex++
#           If present: j = topElements.index(ele)
#           (We need to set j to index of current ele in topElements)
#           (Now move ele up if required)
#           while j >= 1:
#               if freqMap[topElements[j]] > freqMap[topElements[j-1]]:
#                   swap and j--
#               else: break
#        return topElements[0:min(i, k-1)+1]
# Complexity : O(n * k)


def kTop(arr, n, k):
    topElements = [0] * (k + 1)
    freqMap = dict()
    lastIndex = 0

    for i in range(n):
        ele = arr[i]
        if ele in freqMap.keys():
            freqMap[ele] += 1
        else:
            freqMap[ele] = 1

        if ele not in topElements:
            topElements[lastIndex] = ele
            j = lastIndex
            if lastIndex < k:
                lastIndex += 1
        else:
            j = topElements.index(ele)

        while j >= 1:
            if freqMap[topElements[j]] > freqMap[topElements[j-1]]:
                topElements[j], topElements[j-1] = topElements[j-1], topElements[j]
                j -= 1
            else:
                break

        print(topElements[0:min(i, k-1)+1])


if __name__ == "__main__":
    k = 4
    arr = [5, 2, 1, 3, 2, 7, 7, 8, 9, 10, 7, 1]
    n = len(arr)
    kTop(arr, n, k)
