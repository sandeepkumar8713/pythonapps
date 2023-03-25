# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# Question : Alice has n balloons arranged on a rope. You are given a 0-indexed string
# colors where colors[i] is the color of the ith balloon.
# Alice wants the rope to be colorful. She does not want two consecutive balloons to
# be of the same color, so she asks Bob for help. Bob can remove some balloons from the
# rope to make it colorful. You are given a 0-indexed integer array neededTime where
# neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from
# the rope. Return the minimum time Bob needs to make the rope colorful.
#
# Example : Input: colors = "aabaa", neededTime = [1,2,3,4,1]
# Output: 2
# Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1
# second to remove. There are no longer two consecutive balloons of the same color.
# Total time = 1 + 1 = 2.
#
# Question Type : ShouldSee
# Used : Run a single loop while keeping track of current index.
#           If current index and next index values are same, remove the balloon whose cost
#           is less and update current index accordingly.
#        While looping keep track of cost of removed balloons.
# Complexity : O(n)


def find_min_time(colors, neededTime):
    total_time = 0
    current_index = 0
    for next_index in range(1, len(colors)):
        if colors[current_index] == colors[next_index]:
            if neededTime[current_index] <= neededTime[next_index]:
                # remove current_index
                total_time += neededTime[current_index]
                current_index = next_index
            else:
                # remove next_index
                total_time += neededTime[next_index]
        else:
            # no removal required
            current_index = next_index

    return total_time


if __name__ == "__main__":
    colors = "aabaa"
    neededTime = [1, 2, 3, 4, 1]
    print(find_min_time(colors, neededTime))

    colors = "aaa"
    neededTime = [2, 1, 4]
    print(find_min_time(colors, neededTime))

    colors = "a"
    neededTime = [1]
    print(find_min_time(colors, neededTime))
