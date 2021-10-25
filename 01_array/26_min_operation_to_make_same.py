# https://www.geeksforgeeks.org/minimum-number-increment-operations-make-array-elements-equal/
# Question : We are given an array consisting of n elements. At each operation you can
# select any one element and increase rest of n-1 elements by 1. You have to make all
# elements equal performing such operation as many times you wish. Find the minimum number
# of operations needed for this.
#
# Question Type : Easy
# Used : If we took a closer look at each operation as well problem statement we will find that
#        increasing all n-1 element except the largest one is similar to decreasing the largest
#        element only. So, the smallest elements need not to decrease any more and rest of elements
#        will got decremented upto smallest one. In this way the total number of operation required
#        for making all elements equal will be arraySum - n * (smallestElement)
#        minOperation = totalSum - (n * smallest)
# Complexity : O(n)


def minOp(arr, n):
    totalSum = sum(arr)
    smallest = min(arr)

    minOperation = totalSum - (n * smallest)

    return minOperation


if __name__ == "__main__":
    arr = [5, 6, 2, 4, 3]
    n = len(arr)
    print("Minimum Operation = ", minOp(arr, n))
