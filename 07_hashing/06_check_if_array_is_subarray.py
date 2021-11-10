# Question : Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset
# of arr1[] or not. Both the arrays are not in sorted order. It may be assumed that elements
# in both array are distinct.
#
# Examples:
# Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
# Output: arr2[] is a subset of arr1[]
#
# Question Type : Easy
# Used : Python sets are implemented as hash tables.
#        Make a set of elements in arr1. Loop over elements in
#           arr2 and check if element is present in set else return false.
#        If the above case is passed then return true.
# Complexity : O(n)

def isSubset(arr1, arr2):
    hashSet = set()
    for item in arr1:
        hashSet.add(item)

    for key in arr2:
        if key not in hashSet:
            return False

    return True


if __name__ == "__main__":
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
    print(isSubset(arr1, arr2))
