# https://www.geeksforgeeks.org/find-the-maximum-of-minimums-for-every-window-size-in-a-given-array/
# Question : Given an integer array of size n, find the maximum of the minimum's of every
# window size in the array. Note that window size varies from 1 to n.
#
# Input:  arr[] = {10, 20, 30, 50, 10, 70, 30}
# Output:         70, 30, 20, 10, 10, 10, 10
#
# First element in output indicates maximum of minimums of all  windows of size 1.
# Minimums of windows of size 1 are {10}, {20}, {30}, {50}, {10}, {70} and {30}.  Maximum of these minimums is 70
#
# Second element in output indicates maximum of minimums of all  windows of size 2.
# Minimums of windows of size 2 are {10}, {20}, {30}, {10}, {10}, and {30}.  Maximum of these minimums is 30
#
# Third element in output indicates maximum of minimums of all windows of size 3.
# Minimums of windows of size 3 are {10}, {20}, {10}, {10} and {10}. Maximum of these minimums is 20
#
# Similarly other elements of output are computed.
#
# Question Type : OddOne
# Used : set left = [-1] * (n+1) and right = [n] * (n+1)
#       1. Find indexes of next smaller and previous smaller for every element. Next smaller
#          is the nearest smallest element on right side of arr[i]. Similarly, previous smaller
#          element is the nearest smallest element on left side of arr[i]. (by using stack)
#       2. Create an auxiliary array ans[n+1] to store the result. Values in ans[] can be filled
#          by iterating through right[] and left[]
#       3. Once we have indexes of next and previous smaller, we know that arr[i] is a minimum of
#          a window of length "right[i] - left[i] - 1". Lengths of windows for which the elements
#          are minimum are {7, 3, 2, 1, 7, 1, 2}. This array indicates, first element is minimum
#          in window of size 7, second element is minimum in window of size 3, and so on.
#          ans[length] = max(ans[length], inpArr[i])
#       4. Observation:
#       a) Result for length i, i.e. ans[i] would always be greater or same as result for
#          length i+1, i.e., ans[i+1].
#       b) If ans[i] is not filled it means there is no direct element which is minimum of
#          length i and therefore either the element of length ans[i+1], or ans[i+2],
#          and so on is same as ans[i]. So we fill rest of the entries using below loop.
#          for i in range(n-1, 0, -1):
#               ans[i] = max(ans[i], ans[i+1])
#       5) print ans[1:]
# Complexity : O(n)


def printMaxOfMin(inpArr):
    n = len(inpArr)
    left = [-1] * (n+1)
    right = [n] * (n+1)
    stack = []

    # Store previous smaller in left
    # Keep popping out of stack if larger value is found
    for i in range(n):
        while len(stack) != 0 and inpArr[stack[-1]] >= inpArr[i]:
            stack.pop()

        if len(stack) != 0:
            left[i] = stack[-1]

        stack.append(i)

    stack = []

    # Store next smaller in right
    for i in range(n-1, -1, -1):
        while len(stack) != 0 and inpArr[stack[-1]] >= inpArr[i]:
            stack.pop()

        if len(stack) != 0:
            right[i] = stack[-1]

        stack.append(i)

    ans = [0] * (n+1)
    for i in range(n):
        length = right[i] - left[i] - 1
        ans[length] = max(ans[length], inpArr[i])

    # This is for fill up any zero
    for i in range(n-1, 0, -1):
        ans[i] = max(ans[i], ans[i+1])

    print(ans[1:])


if __name__ == "__main__":
    inpArr = [10, 20, 30, 50, 10, 70, 30]
    printMaxOfMin(inpArr)
