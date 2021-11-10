# https://www.geeksforgeeks.org/given-two-unsorted-arrays-find-pairs-whose-sum-x/
# Question : Given two unsorted arrays of distinct elements, the task is to find
# all pairs from both arrays whose sum is equal to x.
#
# Input :  arr1[] = {-1, -2, 4, -6, 5, 7}
#          arr2[] = {6, 3, 4, 0}
#          x = 8
# Output : 4 4
#          5 3
#
# Question Type : Easy
# Used : Loop over the smaller array, add elements to the set.
#        Loop over the larger array, check if sum - element is present in set. Print if present.
# Complexity : O(n)


def findAllPair(arr1, arr2, x):
    hashSet = set()

    if len(arr1) <= len(arr2):
        smallArr = arr1
        largeArr = arr2
    else:
        smallArr = arr2
        largeArr = arr1

    for ele in smallArr:
        hashSet.add(ele)

    for ele in largeArr:
        if x - ele in hashSet:
            print(ele, x - ele)


if __name__ == "__main__":
    arr1 = [-1, -2, 4, -6, 5, 7]
    arr2 = [6, 3, 4, 0]
    x = 8
    findAllPair(arr1, arr2, x)
