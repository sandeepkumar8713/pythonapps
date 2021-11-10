# CTCI : Q16_21_Sum_Swap
# Question : Given two arrays of integers, find a pair of values (one value from each array)
# that you can swap to give the two arrays the same sum.
#
# Input : A[] = {4, 1, 2, 1, 1, 2}
#         B[] = (3, 6, 3, 3)
# Output : {1, 3}
#
# Question Type : ShouldSee
# Used : Find smaller of the 2 array. Find the value that these 2 sum up using this formula
#        diff = abs(sum(largeArr) - sum(smallArr)) / 2
#        Now loop through larger array while checking if (arr[i] + diff or arr[i] - diff)
#           is in smaller array. If found put in pairs dict.
#        If pairs dict is empty then not found else print the pairs.
# Complexity : O(n)


def findPair(arr1, arr2):
    pairs = {}
    if len(arr1) <= len(arr2):
        smallArr = arr1
        largeArr = arr2
    else:
        smallArr = arr2
        largeArr = arr1
    diff = abs(sum(largeArr) - sum(smallArr)) / 2
    for ele in largeArr:
        # This is the main logic
        if ele + diff in smallArr:
            pairs[ele + diff] = ele
        if ele - diff in smallArr:
            pairs[ele - diff] = ele

    for key, value in pairs.items():
        print("smaller array: %s larger array: %s" % (key, value))

    if len(pairs) == 0:
        print("pair not found")


if __name__ == "__main__":
    # arr1 = [4, 1, 2, 1, 1, 2]  # 11
    # arr2 = [3, 6, 3, 3]  # 15

    arr1 = [1, 2, 3, 8]   # 14
    arr2 = [5, 7, 4, 6]   # 22
    findPair(arr1, arr2)
