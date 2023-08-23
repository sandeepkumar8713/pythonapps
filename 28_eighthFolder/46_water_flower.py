# https://leetcode.com/discuss/interview-question/356449/google-oa-2019-watering-flowers-old-version
# Question : You are a gardener and you take care of your plants. The plants are planted in a row and each of them
# needs a specific amount of water. You are about to water them using a watering can. To avoid mistakes like applying
# too much water, or not watering a plant at all, you have decided to:
# 1. water the plants in the order in which they appear, from left to right;
# 2. water each plant if you have sufficient water for it, otherwise refill your watering can;
# 3. water each plant in one go, i.e. without taking a break to refill the watering can in the middle of watering
#    a single plant. This means that you may sometimes have to refill your watering can before or after watering a
#    plant, even though it's not completely empty.
#
# You start at the water container, which is positioned one step before the first plant. How many steps will you take,
# in order to water all the plants in the row? You must take one step to move to the next or the previous plant
# (all plants are positioned one step apart from each other).
#
# Given an array plants of n integers (for the amount of water needed by each plan) and the watering can capacity,
# return the number of steps needed to water all the plants.
#
# Example: Input: plants = [2, 4, 5, 1, 2], capacity = 6
# Output: 17
# Explanation:
# First you water plants[0] and plants[1] (2 steps).
# Then you have to go back to refill (2 steps) and water plants[2] and plants[3] (4 steps).
# Then again you have to refill (4 steps) and water plants[4] (5 steps).
# So 2 + 2 + 4 + 4 + 5 = 17.
#
# Question Type : Generic
# Used : Run a loop over the input array.
#           While doing so keep incrementing steps as well.
#           Also keep updating current_capacity of bucket.
#           Once it becomes negative, add (2 * i) to step count.
#        After the loop return step.
# Logic: for i in range(n):
#        if current_cap >= plants[i]:
#           current_cap -= plants[i]
#        else:
#           steps += (2 * i)
#           current_cap = capacity - plants[i]
#        steps += 1
#        return steps
# Complexity : O(n)


def find_min_steps(plants, capacity):
    n = len(plants)
    current_cap = capacity
    steps = 0
    for i in range(n):
        if current_cap >= plants[i]:
            current_cap -= plants[i]
        else:
            steps += (2 * i)
            current_cap = capacity - plants[i]
        steps += 1

    return steps


if __name__ == "__main__":
    plants = [2, 4, 5, 1, 2]
    capacity = 6
    print (find_min_steps(plants, capacity))

    plants = [2, 2, 1, 1, 2]
    capacity = 3
    print(find_min_steps(plants, capacity))

    plants = [1, 1, 1, 2]
    Capacity = 4
    print(find_min_steps(plants, capacity))
