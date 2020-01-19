# https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
# Question : Given an array of integers, write a function that returns true if there is a triplet (a, b, c)
# that satisfies a2 + b2 = c2.
#
# Question Type : Easy
# Used : convert the given array in square, sort it
#        Fix the last element, find the pair whose sum is equal to last element
#        if above statement fails, repeat with second last element
# Complexity : O(n^2)


def isTriplet(arr, n):
    for i in range(n):
        arr[i] = arr[i] * arr[i]
    arr.sort()
    # fix one element and find other two i goes from n - 1 to 2
    for i in range(n - 1, 1, -1):
        j = 0
        k = i - 1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                return True
            else:
                if arr[j] + arr[k] < arr[i]:
                    j = j + 1
                else:
                    k = k - 1

    return False


if __name__ == "__main__":
    arr = [3, 1, 4, 6, 5]
    arrSize = len(arr)
    print(isTriplet(arr, arrSize))

