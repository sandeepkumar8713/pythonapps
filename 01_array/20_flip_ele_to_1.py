# https://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/
# Question : Given a binary array and an integer m, find the position of zeroes flipping which creates
# maximum number of consecutive 1's in array.
#
# Input:   arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
#          m = 2
# Output:  5 7
# We are allowed to flip maximum 2 zeroes. If we flip arr[5] and arr[7], we get 8 consecutive 1's which is
# maximum possible under given constraints
#
# Question Type : Generic
# Used : Take a sliding window, traverse over the array and keep track of largest window found yet.
#        Take two endpoints of window wLeft, wRight as 0. Also keep track of zeroCount in window.
#        Loop while wRight < n:
#           If zeroCount <= m then check if arr[wRight] is 0, increment zeroCount. Increment window in right side.
#           If zeroCount > m then check if arr[wLeft] is 0, decrement zeroCount. Increment window in left side.
#           Update max window size by comparing it with (wRight - wLeft)
#       Run loop from 0 to bestWindow
#           print bestL + i, if arr[bestL + i] is 0
# Complexity : O(n)


def findZeroes(arr, m):
    n = len(arr)
    wLeft = 0
    wRight = 0

    bestL = bestWindow = 0
    zeroCount = 0

    while wRight < n:
        if zeroCount <= m:
            if arr[wRight] == 0:
                zeroCount += 1
            wRight += 1

        if zeroCount > m:
            if arr[wLeft] == 0:
                zeroCount -= 1
            wLeft += 1

        if (wRight - wLeft) > bestWindow:
            bestWindow = wRight - wLeft
            bestL = wLeft

    for i in range(0, bestWindow):
        if arr[bestL + i] == 0:
            print(bestL + i, end=" ")


if __name__ == "__main__":
    arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
    m = 2
    print("Indexes of zeroes to be flipped are")
    findZeroes(arr, m)
