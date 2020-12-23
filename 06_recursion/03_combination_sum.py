# Question : Given an array of integers A and a sum B, find all unique combinations in A where
# the sum is equal to B. Such number in A may only be used once in the combination.
#
# Question Type : Generic
# Used : Sort the given input array and call recursive findNumbers()
#        In findNumbers if sum is -ve return.
#             If sum is O then add intermediate result in main result(1 possible combination found)
#        In findNumbers() loop over the elements.
#            if given element is less than or equal to sum, then insert the element in intermediate result
#            call findNumbers() again with (sum - arr[i]) and index i+1. If element is duplicate then i+2.
#            pop 1 element from intermediate result
#        findNumbers(arr, sum, r, i):
#        if sum < 0: return
#        if sum == 0: new_list = r[:]
#           res.append(new_list)
#           return
#        while i < len(arr) and sum - arr[i] >= 0:
#           r.append(arr[i])
#           findNumbers(arr, sum - arr[i], r, i+1)
#           if arr[i] == arr[i+1]: i += 2
#           else: i += 1
#           r.pop()
# Complexity : O(2^n)


res = []


def findNumbers(arr, sum, r, i):
    if sum < 0:
        return
    if sum == 0:
        new_list = r[:]
        res.append(new_list)
        return

    while i < len(arr) and sum - arr[i] >= 0:
        r.append(arr[i])
        findNumbers(arr, sum - arr[i], r, i+1)

        if arr[i] == arr[i+1]:
            # Do not start with repeated number
            i += 2
        else:
            i += 1
        r.pop()


if __name__ == "__main__":
    inpArr = [10, 1, 2, 7, 6, 1, 5]
    inpArr.sort()
    r = []
    findNumbers(inpArr, 8, r, 0)
    for item in res:
        print(item)
