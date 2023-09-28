# https://leetcode.com/discuss/interview-question/3848576/Microsoft-Oa
# Question : A car manufacturer has data about the production processes of N different cars
# (numbered from 0 to N-1) and wants to maximize the number of cars produced in the upcoming month. The manufacturing
# information is described by an array H, where H[K] denotes the number of hours required to produce the K-th car.
# There are two assembly lines in the factory, the first of which works for X, and the second Y, hours in a month.
# Every car can be constructed using either one of these lines. Only one car at a time can be produced on each
# assembly line and it is not possible to switch lines after starting the car's production.
# What is the maximum number of different cars that can be produced in the upcoming month?
#
# Given H=[6, 5, 5, 4, 3], X = 8, Y = 9, the answer should be 4. The cars that need 3 and 5 hours can be produced
# on the first assembly line while the second car that needs 5 hours and the car that needs 4 hours can be
# produced using the second line.
#
# TODO : add used
# Used : Run DP with DFS.
#        3 conditions are possible:
#           Include the car in x line
#           Include the car in y line
#           Exclude the car
#        Find max of the above three.
#        For memory use dict dp with key being tuple (index, x, y)


# def max_cars(inp_hours, x, y):
#     if x > y:
#         x, y = y, x
#     # y is larger than x
#
#     dp = [False] * (x + 1)
#     dp[0] = True
#     total = 0
#     max_x = 0
#     count = 0
#     for hour in inp_hours:
#         total += hour
#         if hour > y or total > (x + y):
#             break
#
#         if hour <= x:
#             print (f"hour {hour}")
#             for i in range(x, hour-1, -1):
#                 print (i)
#                 if dp[i - hour]:
#                     dp[i] = True
#                     max_x = max(max_x, i)
#
#         if (total - max_x) > y:
#             break
#
#         count += 1
#
#     return count

import sys


def max_cars(hours, x, y):
    n = len(hours)
    dp = {}

    def dfs(index, x, y):
        if index == n:
            return 0

        hour = hours[index]
        if (index, x, y) in dp:
            return dp[(index, x, y)]

        x_val = -sys.maxsize
        y_val = -sys.maxsize

        if x - hour >= 0:
            # included
            x_val = 1 + dfs(index + 1, x - hour, y)

        if y - hour >= 0:
            # included
            y_val = 1 + dfs(index + 1, x, y - hour)

        # excluded
        not_included = dfs(index + 1, x, y)

        dp[(index, x, y)] = max(max(x_val, y_val), not_included)
        return dp[(index, x, y)]

    return dfs(0, x, y)


if __name__ == "__main__":
    hours = [6, 5, 5, 4, 3]
    x = 8
    y = 9
    print(max_cars(hours, x, y))

    hours = [1, 1, 3]
    x = 1
    y = 1
    print(max_cars(hours, x, y))

    hours = [6, 5, 2, 1, 8]
    x = 17
    y = 5
    print(max_cars(hours, x, y))

    hours = [5, 5, 4, 6]
    x = 8
    y = 8
    print(max_cars(hours, x, y))

    hours = [9, 1, 1]
    x = 1
    y = 1
    print(max_cars(hours, x, y))
