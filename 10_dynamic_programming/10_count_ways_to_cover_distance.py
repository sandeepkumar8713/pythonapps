# CTCI : Q8_01_Triple_Step
# https://leetcode.com/problems/climbing-stairs/
# Question : Given a distance dist, count total number of ways to cover the distance with 1, 2 and 3 steps.
#
# Input:  n = 3
# Output: 4
# Below are the four ways
#  1 step + 1 step + 1 step
#  1 step + 2 step
#  2 step + 1 step
#  3 step
#
# Question Type : ShouldSee
# Used : We have to make a memory table count : size (n+1). Mark all as 0. Initialize base values.
#        Mark count[0] = 1, count[1] = 1, count[2] = 2
#        Loop over the remaining elements, the count[i] would be sum of 3 previous counts
#           as 1, 2, 3 steps are allowed.
#        return count[n]
# Complexity : O(n)


def printCountDP(dist):
    count = [0] * (dist + 1)

    count[0] = 1
    count[1] = 1
    count[2] = 2

    for i in range(3, dist + 1):
        count[i] = (count[i - 1] + count[i - 2] + count[i - 3])

    return count[dist]


if __name__ == "__main__":
    dist = 4
    print("All possible ways are:", printCountDP(dist))
