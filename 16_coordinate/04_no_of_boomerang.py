# https://leetcode.com/problems/number-of-boomerangs/
# Question : You are given n points in the plane that are all distinct, where points[i] = [xi, yi].
# A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance
# between i and k (the order of the tuple matters). Return the number of boomerangs.
#
# Example : Input: points = [[0,0],[1,0],[2,0]]
# Output: 2
# Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
#
# Question Type : Generic
# Used : Run two loops i : 0 to n-1 and j : i to n-1 over the given points
#        Find dist b/w two points and add the dist as key and indices as value(set)
#        in dict. If same dist is present in dict, check if indices overlap in value.
#        If yes, increment the res by 2.
#        After loop, return res
#        Logic :
#        for i in range(0, n - 1):
#           for j in range(i + 1, n):
#               dist_ij = distance(points[i], points[j])
#               if dist_ij in distIndex:
#                   if i in distIndex[dist_ij] or j in distIndex[dist_ij]:
#                       res += 2
#                   else: distIndex[dist_ij] = set()
#               distIndex[dist_ij].add(i)
#               distIndex[dist_ij].add(j)
#        return res
# Complexity : O(n^2) where n is number of points


import math


def distance(pointI, pointJ):
    return math.sqrt((pointI[0] - pointJ[0]) ** 2 + (pointI[1] - pointJ[1]) ** 2)


def numberOfBoomerangs(points):
    if len(points) < 3:
        return 0

    distIndex = {}
    res = 0
    n = len(points)
    for i in range(0, n-1):
        for j in range(i + 1, n):
            dist_ij = distance(points[i], points[j])
            if dist_ij in distIndex:
                if i in distIndex[dist_ij] or j in distIndex[dist_ij]:
                    res += 2
            else:
                distIndex[dist_ij] = set()
            distIndex[dist_ij].add(i)
            distIndex[dist_ij].add(j)

    return res


if __name__ == "__main__":
    points = [[0, 0], [1, 0], [2, 0]]
    print(numberOfBoomerangs(points))

    points = [[1, 1], [2, 2], [3, 3]]
    print(numberOfBoomerangs(points))

    points = [[1, 1]]
    print(numberOfBoomerangs(points))
