# https://leetcode.com/problems/paint-house-iii/
# Question : There is a row of m houses in a small city, each house must be painted with one of the n colors
# (labeled from 1 to n), some houses that have been painted last summer should not be painted again.
# A neighborhood is a maximal group of continuous houses that are painted with the same color.
# For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
# Given an array houses, an m x n matrix cost and an integer target where:
# houses[i]: is the color of the house i, and 0 if the house is not painted yet.
# cost[i][j]: is the cost of paint the house i with the color j + 1.
# Return the minimum cost of painting all the remaining houses in such a way that there are exactly target
# neighborhoods. If it is not possible, return -1.
#
# Question Type : Should See
# Used : We will use DP with DFS.
#        We will start at first house, then try to paint it will all possible colors and then do DFS on next house.
#        After DFS on second house, we will choose least cost and save in memory table.
#        If house is already painted, we get the cost of next house.
#        When prev_color and current_color changes, we should increment group count.
# Logic: def dfs(house_index, prev_color, group_count):
#        if house_index == house_count and group_count == target: return 0
#        if house_index >= house_count or group_count > target: return sys.maxsize
#        if (house_index, prev_color, group_count) in memo_dict.keys():
#           return memo_dict.get((house_index, prev_color, group_count))
#        if houses[house_index] == 0:
#           for curr_color in range(1, color_count + 1):
#               if prev_color != curr_color:
#                   color_cost = dfs(house_index + 1, curr_color, group_count + 1) + cost[house_index][curr_color - 1]
#               else:
#                   color_cost = dfs(house_index + 1, curr_color, group_count) + cost[house_index][curr_color - 1]
#               result = min(result, color_cost)
#        else:
#           curr_color = houses[house_index]
#           if prev_color != curr_color:
#               result = dfs(house_index + 1, curr_color, group_count + 1)
#           else:
#               result = dfs(house_index + 1, curr_color, group_count)
#        memo_dict[(house_index, prev_color, group_count)] = result
#        return result
#
#        ans = dfs(0, 0, 0)
# Complexity : O(m*n*k) where m is number of houses, n is number of colors and k is number of groups

import sys


def min_paint_cost(houses, cost, house_count, color_count, target):
    memo_dict = dict()

    # All houses are painted
    if 0 not in houses:
        return -1

    def dfs(house_index, prev_color, group_count):
        if house_index == house_count and group_count == target:
            return 0
        if house_index >= house_count or group_count > target:
            return sys.maxsize

        if (house_index, prev_color, group_count) in memo_dict.keys():
            return memo_dict.get((house_index, prev_color, group_count))

        result = sys.maxsize
        # not colored house
        if houses[house_index] == 0:
            # Try all colors
            for curr_color in range(1, color_count + 1):
                if prev_color != curr_color:
                    color_cost = dfs(house_index + 1, curr_color, group_count + 1) + cost[house_index][curr_color - 1]
                else:
                    color_cost = dfs(house_index + 1, curr_color, group_count) + cost[house_index][curr_color - 1]
                result = min(result, color_cost)
        else:
            # colored house
            curr_color = houses[house_index]
            if prev_color != curr_color:
                result = dfs(house_index + 1, curr_color, group_count + 1)
            else:
                result = dfs(house_index + 1, curr_color, group_count)

        memo_dict[(house_index, prev_color, group_count)] = result
        return result

    ans = dfs(0, 0, 0)
    return ans


if __name__ == "__main__":
    houses = [0, 0, 0, 0, 0]
    cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    m = 5
    n = 2
    target = 3
    print(min_paint_cost(houses, cost, m, n, target))

    houses = [0, 2, 1, 2, 0]
    cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    m = 5
    n = 2
    target = 3
    print(min_paint_cost(houses, cost, m, n, target))

    houses = [3, 1, 2, 3]
    cost = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    m = 4
    n = 3
    target = 3
    print(min_paint_cost(houses, cost, m, n, target))
