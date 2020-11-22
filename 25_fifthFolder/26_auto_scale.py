# https://leetcode.com/discuss/interview-question/376019/
# Question : A risk modeling system uses a scaling system that implements an auto-scale policy depending on the
# current load or utilization of the computing system. The system starts with a number of computing instances
# given by instances. The system polls the instances every second to see the average utilization at that second,
# and performs scaling as given below. Once any action is taken, the system will stop polling for 10 seconds.
# During that time, the number of instances does not change. Avg utilization > 60% : Double the number of instance
# if the doubled value does not exceed 2*10^8. This is an action. Avg utilization < 25% : Halve the number of
# instances if the number is greater than 1(use ceil). Given th values of the average utilization at each second
# for this system as an array determine the number of instances at the end of the time frame.
#
# Question Type : Easy
# Used : Loop over the given inpArr, if avg util is less than 25%, half the instances. If avg utils is more than 60%,
#        double the instances. After doubling or reducing the instances, increment the loop index by 10.
# Complexity : O(n)

import math
upperLimit = int(1e8)
lowerLimit = 1

def autoScale(instances, avgUtils):
    lowUtilLimit = 25
    highUtilLimit = 60
    i = 0
    while i < len(avgUtils):
        if avgUtils[i] < lowUtilLimit:
            if instances > lowerLimit:
                instances = math.ceil(instances/2)
                i += 9
        elif avgUtils[i] > highUtilLimit:
            if instances <= upperLimit:
                instances = 2 * instances
                i += 9
        i += 1
    return instances


if __name__ == "__main__":
    instances = 1
    avgUtils = [5, 10, 80]
    print(autoScale(instances, avgUtils))

    instances = 2
    avgUtils = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]
    print(autoScale(instances, avgUtils))

    instances = 2
    avgUtils = [1, 3, 5, 10, 80]
    print(autoScale(instances, avgUtils))
