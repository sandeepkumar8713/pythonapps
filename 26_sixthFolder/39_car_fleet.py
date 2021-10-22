# https://leetcode.com/problems/car-fleet/
# Similar : https://leetcode.com/problems/car-fleet-ii/
# Question : There are n cars going to the same destination along a one-lane road. The destination
# is target miles away. You are given two integer array position and speed, both of length n,
# where position[i] is the position of the ith car and speed[i] is the speed of the ith car
# (in miles per hour). A car can never pass another car ahead of it, but it can catch up to it,
# and drive bumper to bumper at the same speed. The distance between these two cars is ignored
# (i.e., they are assumed to have the same position). A car fleet is some non-empty set of
# cars driving at the same position and same speed. Note that a single car is also a car fleet.
# If a car catches up to a car fleet right at the destination point, it will still be
# considered as one car fleet. Return the number of car fleets that will arrive at the destination.
#
# Example : Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation: The cars starting at 10 and 8 become a fleet, meeting each other at 12.
# The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 and 3 become a fleet, meeting each other at 6.
# Note that no other cars meet these fleets before the destination, so the answer is 3.
#
# Question Type : ShouldSee
# Used : Make a list of tuples, with two fields, position and time to reach
#        Now sort this list. The last car in this list will reach first.
#        Loop over the list in reverse, the cars whose time_to_reach is less can the first car to reach,
#        will join the fleet. Else that car will form another fleet.
#        After the loop return the fleet count.
#        Logic :
#        for i in range(n):
#           timeRemaining = (target - position[i]) / speed[i]
#           cs.append((position[i], timeRemaining))
#        cs.sort()
#        fleet = 1, time_to_reach = cs[n - 1][1]
#        for i in range(n - 2, -1, -1):
#           if cs[i][1] <= time_to_reach: continue
#           fleet += 1
#           time_to_reach = cs[i][1]
#        return fleet
# Complexity : O(n log n)


def carFleet(target, position, speed):
    n = len(position)
    cs = []

    for i in range(n):
        timeRemaining = (target - position[i]) / speed[i]
        cs.append((position[i], timeRemaining))

    cs.sort()

    fleet = 1
    time_to_reach = cs[n - 1][1]

    for i in range(n - 2, -1, -1):
        if cs[i][1] <= time_to_reach:  # it will join a fleet
            continue
        fleet += 1
        time_to_reach = cs[i][1]

    return fleet


if __name__ == "__main__":
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(carFleet(target, position, speed))

    target = 10
    position = [3]
    speed = [3]
    print(carFleet(target, position, speed))
