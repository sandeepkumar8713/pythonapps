# https://www.geeksforgeeks.org/find-elemepnt-array-sum-left-array-equal-sum-right-array/
# Question : Given, an array of size n. Find an element which divides the array in two sub-arrays with equal sum.
#
# Used : First make a right sum while excluding the first element. Now loop through the array while subtracting values
#        from right sum and adding previous one to left sum.
# Complexity : O(n)


def findEquilibrium(arr):
    leftSum = 0
    rightSum = sum(arr[1:])

    i=0
    j=1
    while i < len(arr) and j < len(arr):
        rightSum -= arr[j]
        leftSum += arr[i]

        if leftSum == rightSum:
            return i+1

        i += 1
        j += 1
    return -1


if __name__ == "__main__":
    arr = [1, 4, 2, 5]
    print findEquilibrium(arr)
