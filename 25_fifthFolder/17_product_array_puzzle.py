# https://www.geeksforgeeks.org/a-product-array-puzzle/
# Question : Given an array arr[] of n integers, construct a Product Array prod[] (of same size) such that
# prod[i] is equal to the product of all the elements of arr[] except arr[i]. Solve it without division
# operator in O(n) time.
#
# Example : Input: arr[]  = {10, 3, 5, 6, 2}
# Output: prod[]  = {180, 600, 360, 300, 900}
#
# Question Type : Easy
# Used : Make running(cumulative) array of products for left and right elements. Then multiply them to get answer.
#        productArray(arr, n):
#        temp = 1, prod = [1] * n
#        for i in range(n):
#           prod[i] = temp, temp *= arr[i]
#        temp = 1
#        for i in range(n - 1, -1, -1):
#           prod[i] *= temp, temp *= arr[i]
#        return prod
# Complexity : O(n)


def productArray(arr, n):
    if n == 1:
        print(0)
        return

    temp = 1
    prod = [1] * n

    for i in range(n):
        prod[i] = temp
        temp *= arr[i]

    temp = 1
    for i in range(n - 1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]
    print(prod)


if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    n = len(arr)
    productArray(arr, n)
