# https://leetcode.com/problems/koko-eating-bananas/
# Question : Koko loves to eat bananas. There are n piles of bananas, the ith pile has
# piles[i] bananas. The guards have gone and will come back in h hours. Koko can decide
# her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and
# eats k bananas from that pile. If the pile has less than k bananas, she eats all of them
# instead and will not eat any more bananas during this hour. Koko likes to eat slowly but
# still wants to finish eating all the bananas before the guards return. Return the minimum
# integer k such that she can eat all the bananas within h hours.
#
# Example : Input: piles = [3,6,7,11], h = 8
# Output: 4
#
# Question Type : Generic
# Used : Here the aim is to finish all the piles within h hours but with minimum speed.
#        We guess a speed (b/w 1 and max(piles)), check if we can finish all bananas.
#        We need to do Binary search over the guess. While doing so find min speed with
#        all bananas eaten.
#        Logic :
#        def hrsTakes(k, piles):
#        return sum(math.ceil(p / k) for p in piles)
#
#        def minEatingSpeed(piles, h)
#        left, right = 1, max(piles)
#        minK = right
#        while left <= right:
#           mid = (left + right) // 2
#           if hrsTakes(mid, piles) > h:
#               left = mid + 1
#           else:
#               minK = mid
#               right = mid - 1
#        return minK
# Complexity : O(n log n) where n is piles count


import math


def hrsTakes(k, piles):
    return sum(math.ceil(p / k) for p in piles)


def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    minK = right

    while left <= right:
        mid = (left + right) // 2
        if hrsTakes(mid, piles) > h:
            # Can't finish all bananas, so need to increase the speed.
            left = mid + 1
        else:
            # Can finish the banana, but loop more to find lesser speed.
            minK = mid
            right = mid - 1

    return minK


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print(minEatingSpeed(piles, h))
