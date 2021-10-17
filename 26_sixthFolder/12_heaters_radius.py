# https://leetcode.com/problems/heaters/
# Question : Winter is coming! During the contest, your first job is to design a standard heater with a
# fixed warm radius to warm all the houses. Every house can be warmed, as long as the house is within
# the heater's warm radius range. Given the positions of houses and heaters on a horizontal line,
# return the minimum radius standard of heaters so that those heaters could cover all houses.
# Notice that all the heaters follow your radius standard, and the warm radius will the same.
#
# Example : Input: houses = [1,2,3,4], heaters = [1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard,
# then all the houses can be warmed.
#
# Question Type : Generic
# Used : For each house element, run binary search on heater array.
#        While doing so we will get min distance b/w house and heater on each side of the house.
#        Find min of the above. By this way we will get nearest heater for each house.
#        return max of above dist list.
#        Logic :
#        heaters.sort(), ans = 0
#        for house in houses:
#           low = 0, high = len(heaters) - 1
#           ld = sys.maxsize, rd = sys.maxsize
#           while low <= high:
#               mid = (low + high) // 2
#               if heaters[mid] == house:
#                   ld = 0, rd = 0, break
#               elif house < heaters[mid]:
#                   rd = heaters[mid] - house
#                   high = mid - 1
#               else:
#                   ld = house - heaters[mid]
#                   low = mid + 1
#           ans = max(ans, min(ld, rd))
#        return ans
# Complexity : O(n log n)

import sys


def findRadius(houses, heaters):
    heaters.sort()

    ans = 0
    for house in houses:
        low = 0
        high = len(heaters) - 1
        ld = sys.maxsize
        rd = sys.maxsize
        while low <= high:
            mid = (low + high) // 2
            if heaters[mid] == house:
                ld = 0
                rd = 0
                break
            elif house < heaters[mid]:
                rd = heaters[mid] - house
                high = mid - 1
            else:
                ld = house - heaters[mid]
                low = mid + 1

        ans = max(ans, min(ld, rd))

    return ans


if __name__ == "__main__":
    houses = [1, 2, 3, 4]
    heaters = [1, 4]
    print(findRadius(houses, heaters))

    houses = [1, 2, 3]
    heaters = [2]
    print(findRadius(houses, heaters))
