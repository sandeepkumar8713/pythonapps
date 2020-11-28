# https://www.geeksforgeeks.org/binary-indexed-tree-range-updates-point-queries/
# Question : Given an array arr[0..n-1]. The following operations need to be performed.
# update(l, r, val) : Add 'val' to all the elements in the array from [l, r].
# getElement(i) : Find element in the array indexed at 'i'.
# Initially all the elements in the array are 0. Queries can be in any oder, i.e., there can be many updates
# before point query.
#
# Input : arr = {0, 0, 0, 0, 0}
# Queries: update : l = 0, r = 4, val = 2
#          getElement : i = 3
#          update : l = 3, r = 4, val = 3
#          getElement : i = 3
#
# Output: Element at 3 is 2
#         Element at 3 is 5
#
# Explanation : Array after first update becomes
#               {2, 2, 2, 2, 2}
#               Array after second update becomes
#               {2, 2, 2, 5, 5}
#
# Question Type : Generic
# Used : Loop over all the input element and update in BIT(Binary Index Tree) Tree
#        updateBIT():
#        add 1 to i.
#        Loop while i <= n:
#           add val to BITTree[i]
#           i += i & (-i); Add 1 to last set bit of i
#        update():
#        call updateBIT twice with :
#        updateBIT(BITTree, n, l, val) and updateBIT(BITTree, n, r+1, -val)
#        getElement() :
#        add 1 to i.
#        Loop while i >= 0 :
#           data += BITTree[index]
#           i -= i & (-i); Subtract 1 from last set bit of i
#        After the loop return data.
# Complexity :  O(q * log n) + O(n * log n) where q is number of queries.


def updateBIT(BITTree,n,i,val):
    index = i+1
    while index <= n:
        BITTree[index] += val
        inc = index & (-index)
        # Parent can be obtained by adding 1 to the last set bit of index
        index += inc


def constructBITTree(arr,n):
    BITTree = [0] * (n + 1)

    for i in range(len(arr)):
        updateBIT(BITTree, n, i, arr[i])

    return BITTree


def update(BITree, l, r, n, val):
    updateBIT(BITTree, n, l, val)
    updateBIT(BITTree, n, r+1, -val)


def getElement(BITTree, index):
    data = 0
    index += 1
    while index > 0:
        data += BITTree[index]
        dec = index & (-index)
        # Parent can be obtained by subtracting 1 from the last set bit of index
        index -= dec

    return data


if __name__ == "__main__":
    arr = [0, 0, 0, 0, 0]
    n = len(arr)
    BITTree = constructBITTree(arr, n)

    l = 0
    r = 4
    val = 2
    update(BITTree, l, r, n, val)

    index = 3
    print(getElement(BITTree, index))

    l = 3
    r = 4
    val = 3
    update(BITTree, l, r, n, val)

    index = 3
    print(getElement(BITTree, index))
