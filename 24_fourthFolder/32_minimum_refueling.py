# Question : A car travels from a starting position to a destination which is target miles east
# of the starting position. Along the way, there are gas stations. Each station[i] represents
# a gas station that is station[i][0] miles east of the starting position, and has station[i][1]
# liters of gas. The car starts with an infinite tank of gas, which initially has startFuel
# liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives. When the car reaches
# a gas station, it may stop and refuel, transferring all the gas from the station into the car.
# What is the least number of refueling stops the car must make in order to reach its destination?
# If it cannot reach the destination, return -1. Note that if the car reaches a gas station with 0
# fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left,
# it is still considered to have arrived.
#
# Example : Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can't reach the target (or even the first gas station).
#
# Question Type : Generic
# Used : When driving past a gas station, let's remember the amount of fuel it contained. We don't
#        need to decide yet whether to fuel up here or not - for example, there could be a bigger
#        gas station up ahead that we would rather refuel at. When we run out of fuel before
#        reaching the next station, we'll retroactively fuel up: greedily choosing the largest
#        gas stations first.
#        Logic : minRefuelStops(target, tank, stations):
#        pq = []  # A maxheap is simulated using negative values
#        stations.append((target, float('inf')))
#        ans = prev = 0
#        for location, capacity in stations:
#           tank -= location - prev
#           while pq and tank < 0:  # must refuel in past
#               tank += -heapq.heappop(pq)
#               ans += 1
#           if tank < 0: return -1
#           heapq.heappush(pq, -capacity)
#           prev = location
#        return ans
# Complexity : O(n log n)

import heapq


def minRefuelStops(target, tank, stations):
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in past
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0:
                return -1
            heapq.heappush(pq, -capacity)
            prev = location

        return ans


if __name__ == "__main__":
    target = 100
    startFuel = 1
    stations = [[10, 100]]
    print(minRefuelStops(target, startFuel, stations))
