# https://www.geeksforgeeks.org/minimum-number-jumps-reach-endset-2on-solution/
# https://leetcode.com/problems/jump-game-ii/
# Similar : https://leetcode.com/problems/jump-game/
# Similar : https://leetcode.com/problems/coin-path/ https://massivealgorithms.blogspot.com/2017/08/leetcode-656-coin-path.html
# Question : Given an array of integers where each element represents the max number of steps
# that can be made forward from that element. Write a function to return the minimum number
# of jumps to reach the end of the array (starting from the first element).
# If an element is 0, then cannot move through that element.
# Similar : 24_fourthFolder/32_minimum_refueling
#
# Input :  arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output :  3 (1-> 3 -> 9 -> 9)
#
# Question Type : Generic, SimilarAdded
# Used : The idea is to traverse all possible steps, and keep updating maxReach. Once
#        previous point's reach get over. do step = maxReach - i, this way we find the
#        maxReach for this point, by traveling reach(step) of previous point.
# Logic: minJumps(arr) :
#        set step = arr[0], jump = 1.
#        Now run a loop from 1 to n-1 :
#           if i == n-1: return jump
#           maxReach = max(maxReach, i + arr[i])
#           step -= 1   (we are moving forward, reducing our reach)
#           if step == 0: (Our reach is over. Now we have to choose maxReach found till
#                          from the previous point and jump)
#               jump += 1
#               if i >= maxReach: return -1 (Not possible to reach end, step should not be negative)
#               step = maxReach - i
#        return -1
# Complexity : O(n)


def minJumps(arr):
    n = len(arr)
    if n <= 1:
        return 0

    if arr[0] == 0:
        return -1

    # initialization
    # stores all time the maximal reachable index in the array
    maxReach = arr[0]
    # stores the number of steps we can still take
    step = arr[0]
    # stores the number of jumps necessary to reach that maximal reachable position
    jump = 1

    # Start traversing the array
    for i in range(1, n):
        if i == n - 1:
            return jump

        # updating maxReach
        maxReach = max(maxReach, i + arr[i])

        # we use a step to get to the current index
        step -= 1

        # If no further steps left
        if step == 0:
            # print arr[i]
            # we must have used a jump
            jump += 1

            # Check if the current index/position or lesser index
            # is the maximum reach point from the previous indexes
            if i >= maxReach:
                return -1

            # re-initialize the steps to the amount
            # of steps to reach maxReach from position i.
            step = maxReach - i
    return -1


if __name__ == "__main__":
    # arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    arr = [1, 3, 5, 8, 2, 4, 6, 7, 6, 8, 9]
    print("Minimum number of jumps to reach end is %d " % minJumps(arr))
