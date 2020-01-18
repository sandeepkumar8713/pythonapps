# CTCI : Q17_24_Max_Submatrix
# https://www.geeksforgeeks.org/dynamic-programming-set-27-max-sum-rectangle-in-a-2d-matrix/
# http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
# Question : Given a 2D array, find the maximum sum sub array in it. It can contain +ve and -ve numbers
# Kadane algorithm
#
# Loop for each element of the array
#   (a) max_ending_here = max_ending_here + a[i]
#   (b) if(max_ending_here < 0)
#             max_ending_here = 0
#   (c) if(max_so_far < max_ending_here)
#             max_so_far = max_ending_here
# return max_so_far
#
# Used : for all possible combination of columns for start and end, make a temp array containing sum of all the columns
#         in between for each row. Send that row to Kadane algorithm, which will return the max sum its corresponding
#         start and end. Compare it with previously saved max value and update accordingly.
# Complexity : O(n^3)


def kadane(arr):
    maxEndingHere = 0
    maxSoFar = -9999

    maxSoFarStart = -1
    maxSoFarEnd = -1

    maxEndingHereStart = 0
    maxEndingHereEnd = 0
    for i in range(0, len(arr)):
        maxEndingHere += arr[i]
        maxEndingHereEnd = i

        if maxEndingHere < 0:
            maxEndingHere = 0
            maxEndingHereStart = i+1
            maxEndingHereEnd = i+1

        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
            maxSoFarStart = maxEndingHereStart
            maxSoFarEnd = maxEndingHereEnd

    return {'sum': maxSoFar, 'start': maxSoFarStart, 'end': maxSoFarEnd}


def findMaxSum(M):
    col = len(M[1])
    row = len(M)
    maxSum = -9999

    for left in range(0, col):
        temp = [0] * row
        for right in range(left, col):
            for i in range(0, row):
                temp[i] += M[i][right]

            # Find the maximum sum sub array in temp[].
            indexDict = kadane(temp)
            sum = indexDict['sum']
            start = indexDict['start']
            end = indexDict['end']

            if sum > maxSum:
                maxSum = sum
                finalLeft = left
                finalRight = right
                finalTop = start
                finalBottom = end

    print ('sum = %s' % maxSum)
    print ('start = %s,%s' % (finalLeft, finalTop))
    print ('end = %s,%s' % (finalRight, finalBottom))

# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
# print kadane(arr)


if __name__ == "__main__":
    M = [[1, 2, -1, -4, -20],
         [-8, -3, 4, 2, 1],
         [3, 8, 10, 1, 3],
         [-4, -1, 1, 7, -6]]

    findMaxSum(M)
