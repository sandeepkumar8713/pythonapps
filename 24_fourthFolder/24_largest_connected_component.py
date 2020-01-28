# https://github.com/Seanforfun/Algorithm-and-Leetcode/blob/master/leetcode/952.%20Largest%20Component%20Size%20by%20Common%20Factor.md
# Question : Given a non-empty array of unique positive integers A, consider the following graph:
# There are A.length nodes, labelled A[0] to A[A.length - 1];
# There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.
#
# Example : Input: [4,6,15,35]
# Output: 4
#
# Question Type : Generic
# Used : We are using union and find concept. Run a loop over each element in input array. Find all its
#        factors and make union from the element to all its factors.
#        Now run a loop again, find root of each element from union. For connected components all the elements will
#        have same root. So keep the freq of root. Root with max freq is the answer.
#        Suppose elements are 15 and 35, then there uf will be : 35 -> 5 -> 7 and 15 -> 3 -> 5 -> 7. So both will have
#        7 as root.
#        Logic : def largestComponentSize(inpArr):
#        if inpArr is None or len(inpArr) == 0:
#           return 0
#        maxEle = max(inpArr)
#        uf = [0] * (maxEle + 1)
#        for i in range(len(uf)): uf[i] = i
#        for i in range(len(inpArr)):
#           j = 2
#           while j <= math.sqrt(inpArr[i]):
#               if inpArr[i] % j == 0:
#                   union(inpArr[i], j, uf)
#                   union(inpArr[i], inpArr[i] // j, uf)
#               j += 1
#        map = dict(), res = 1
#        for i in range(len(inpArr)):
#           root = find(inpArr[i], uf)
#           if root in map.keys():
#               curr = map[root]
#           else:
#               curr = 0
#           curr += 1
#           map[root] = curr
#           res = max(res, curr)
#        return res
# Complexity : O(n * sqrt(max))

import math


def union(i, j, uf):
    p = find(i, uf)
    q = find(j, uf)
    uf[p] = q


def find(j, uf):
    if uf[j] != j:
        uf[j] = find(uf[j], uf)
    return uf[j]


def largestComponentSize(inpArr):
    if inpArr is None or len(inpArr) == 0:
        return 0
    maxEle = max(inpArr)
    uf = [0] * (maxEle + 1)
    for i in range(len(uf)):
        uf[i] = i

    #  For every number, find their factor and add to uf.
    for i in range(len(inpArr)):
        j = 2
        while j <= math.sqrt(inpArr[i]):
            if inpArr[i] % j == 0:
                union(inpArr[i], j, uf)
                union(inpArr[i], inpArr[i] // j, uf)
            j += 1

    map = dict()
    res = 1
    for i in range(len(inpArr)):
        root = find(inpArr[i], uf)
        if root in map.keys():
            curr = map[root]
        else:
            curr = 0
        curr += 1
        map[root] = curr
        res = max(res, curr)

    return res


if __name__ == "__main__":
    inpArr = [4, 6, 15, 35]
    print(largestComponentSize(inpArr))
