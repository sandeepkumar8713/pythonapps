# https://leetcode.com/problems/remove-boxes/
# Question : You are given several boxes with different colors represented by different
# positive numbers. You may experience several rounds to remove boxes until there is no
# box left. Each time you can choose some continuous boxes with the same color (i.e.,
# composed of k boxes, k >= 1), remove them and get k * k points.
# Return the maximum points you can get.
#
# Input: boxes = [1,3,2,2,2,3,4,3,1]
# Output: 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
# ----> [1, 3, 3, 3, 1] (1*1=1 points)
# ----> [1, 1] (3*3=9 points)
# ----> [] (2*2=4 points)
# TODO :: add code
#