# https://leetcode.com/problems/the-skyline-problem/
# Question : A city's skyline is the outer contour of the silhouette formed by all the buildings in that
# city when viewed from a distance. Given the locations and heights of all the buildings, return the
# skyline formed by these buildings collectively.
# The geometric information of each building is given in the array buildings where buildings[i] =
# [lefti, righti, heighti]:
# lefti is the x coordinate of the left edge of the ith building.
# righti is the x coordinate of the right edge of the ith building.
# heighti is the height of the ith building.
# You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
#
# Example : Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
#
# Question Type : ShouldSee
# Used : Transition point tp (0 and 1) where building start and ends
#        Loop over the given building list, make 2 tuples of left, tp, height, and index and append it in list.
#        Loop over the sorted list
#           if building is starting, push h(height) and i(index) in maxHeap.
#           check if curr_height needs to be updated and if yes append the x and curr_height in res_list
#           set alive[i] to true
#           else:
#           set alive[i] to false
#           pop dead nodes from the maxHeap
#           If nodes are still present in maxHeap,
#               check if curr_height needs to be updated and if yes append the x and curr_height in res_list
#           else if maxHeap is empty,
#              set curr_height = 0, append the x and curr_height in res_list
#        return res_list
#        Logic:
#        for l, r, h in buildings:
#           hs.append((l, 0, -h, i))
#           hs.append((r, 1, h, i))
#           i += 1
#        hs.sort()
#        for x, tp, h, i in hs:
#        if tp == 0:
#           heapq.heappush(heap, (h, i))
#           alive[i] = True
#           if current_height < -h:
#               res.append([x, -h]), current_height = -h
#        else:
#           alive[i] = False
#           while heap and not alive[heap[0][1]]:
#               heapq.heappop(heap)
#           if heap and -heap[0][0] < current_height:
#               current_height = -heap[0][0], res.append([x, current_height])
#           elif not heap:
#               current_height = 0, res.append([x, current_height])
#        return res
# Complexity : O(n log n)

import heapq


# tp : transition point
def getSkyline(buildings):
    N, hs = len(buildings), []
    i = 0
    for l, r, h in buildings:
        hs.append((l, 0, -h, i))
        hs.append((r, 1, h, i))
        i += 1
    hs.sort()
    alive = [False] * N

    res, heap, current_height = [], [], 0
    for x, tp, h, i in hs:
        if tp == 0:  # start of i-th building
            heapq.heappush(heap, (h, i))
            alive[i] = True
            if current_height < -h:
                res.append([x, -h])
                current_height = -h
        else:  # end of i-th building
            alive[i] = False
            while heap and not alive[heap[0][1]]:
                heapq.heappop(heap)
            if heap and -heap[0][0] < current_height:
                current_height = -heap[0][0]
                res.append([x, current_height])
            elif not heap:
                current_height = 0
                res.append([x, current_height])
    return res


if __name__ == "__main__":
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(getSkyline(buildings))
