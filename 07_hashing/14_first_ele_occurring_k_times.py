# Question : Given an array of n integers. The task is to find the first element that
# occurs k number of times. If no element occurs k times the print -1. The distribution
# of integer elements could be in any range.
#
# Input : {1, 7, 4, 3, 4, 8, 7}
#         k = 2
# Output : 7
#
# Question Type : Easy
# Used : Loop over the elements in input array and update its frequency in hashDict.
#        Loop again over the elements in input array and return element if its
#           frequency equal with k.
#        If loop got over return -1.
# Complexity : O(n)


def findFirstEle(inpArr, k):
    hashDict = dict()
    for ele in inpArr:
        if ele in hashDict.keys():
            hashDict[ele] += 1
        else:
            hashDict[ele] = 1

    for ele in inpArr:
        if hashDict[ele] == k:
            return ele
    return -1


if __name__ == "__main__":
    inpArr = [1, 7, 4, 3, 4, 8, 7]
    k = 2
    print(findFirstEle(inpArr, k))
