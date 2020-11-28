# https://careercup.com/question?id=5660935302152192
# https://leetcode.com/discuss/interview-question/699973/
# Question : You are given 2 arrays: one representing the time people arrive at a door and other representing
# the direction they want to go(in or out) You have to find at what time each person will use the door provided
# no 2 people can use the door at the same time. Constraints: the door starts with ‘in’ position, in case of a
# conflict(2 or more people trying to use the door at the same time), the direction previously used holds precedence.
# If there is no conflict whoever comes first uses the door. Also if no one uses the door, it reverts back to the
# starting ‘in’ position. Should be linear time complexity.
#
# Question Type : ShouldSee
# Used : Do Pre-processing of the given time and direction list. Make a 2D Dictionary, with value as
#        person id : {"arrivalTime":{"In":[0],"Out":[1]}}
#        Now loop over the outer dict, from min to max arrival time, keep track of usageTime
#        and current Direction. Allow people to go whose desired direction is currDir then flip
#        currDir then allow other set of people to go.
#        assignUsageTime(arrivalMap, minTime, maxTime):
#        currDir = "In", usageTime = minTime
#        for time in range(minTime, maxTime + 1):
#           if time not in arrivalMap:
#               if time > usageTime: usageTime=time + 1, currDir = "In"
#               continue
#           directionMap = arrivalMap[time]
#           for personId in directionMap[currDir]:
#               print(usageTime, personId, currDir), usageTime += 1
#           currDir = flipDirection(currDir)
#           for personId in directionMap[currDir]:
#               print(usageTime, personId, currDir), usageTime += 1
# Complexity : O(n)

def flipDirection(currDir):
    if currDir == "In":
        return "Out"
    else:
        return "In"


def assignUsageTime(arrivalMap, minTime, maxTime):
    currDir = "In"
    usageTime = minTime
    for time in range(minTime, maxTime + 1):
        if time not in arrivalMap:
            if time > usageTime:
                usageTime = time + 1
                currDir = "In"
            continue
        directionMap = arrivalMap[time]
        for personId in directionMap[currDir]:
            print(usageTime, personId, currDir)
            usageTime += 1
        currDir = flipDirection(currDir)
        for personId in directionMap[currDir]:
            print(usageTime, personId, currDir)
            usageTime += 1


def getDoorUsageTime(time, direction):
    arrivalMap = dict()
    minTime = min(time)
    maxTime = max(time)
    for i in range(len(time)):
        if time[i] not in arrivalMap:
            arrivalMap[time[i]] = {"In": [], "Out": []}
        arrivalMap[time[i]][direction[i]].append(i)
    assignUsageTime(arrivalMap, minTime, maxTime)


if __name__ == "__main__":
    time =       [2,    3,     5,     1,     7,   4,      2]
    direction = ["In", "Out", "In", "Out", "Out", "In", "Out"]

    getDoorUsageTime(time, direction)
