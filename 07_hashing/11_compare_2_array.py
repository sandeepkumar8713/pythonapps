# Question : Given two given arrays of equal length, the task is to find if given arrays are equal or not.
# Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation)
# of elements may be different though.
#
# Question Type : Easy
# Used : Loop over the elements of arr1 and make a entry of its frequency in hash dict.
#        Loop over the elements of arr2 and see if it is present in hash dict and reduce its frequency by 1 else
#           return False
#        Return true if above condition is passed.
# Complexity : O(n)


def areEqual(arr1, arr2):
    hashDict = dict()
    for ele in arr1:
        if ele in hashDict.keys():
            hashDict[ele] += 1
        else:
            hashDict[ele] = 1

    for ele in arr2:
        if ele in hashDict.keys():
            hashDict[ele] -= 1
            if hashDict[ele] == 0:
                del hashDict[ele]
        else:
            return False

    return True


if __name__ == "__main__":
    arr1 = [1, 2, 5, 4, 0, 2, 1]
    arr2 = [2, 4, 5, 0, 1, 1, 2]
    print(areEqual(arr1, arr2))

