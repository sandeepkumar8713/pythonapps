# https://www.geeksforgeeks.org/assembly-line-scheduling-dp-34/
# Question : A car factory has two assembly lines, each with n stations. A station is denoted by Si,j where i
# is either 1 or 2 and indicates the assembly line the station is on, and j indicates the number of the station.
# The time taken per station is denoted by ai,j. Each station is dedicated to some sort of work like engine fitting,
# body fitting, painting, and so on. So, a car chassis must pass through each of the n stations in order before
# exiting the factory. The parallel stations of the two assembly lines perform the same task. After it passes
# through station Si,j, it will continue to station Si,j+1 unless it decides to transfer to the other line.
# Continuing on the same line incurs no extra cost, but transferring from line i at station j – 1 to station j on
# the other line takes time ti,j. Each assembly line takes an entry time ei and exit time xi which may be different
# for the two lines. Give an algorithm for computing the minimum time it will take to build a car chassis.
#
# Question Type : ShouldSee
# Used : At each station of each assembly line, calculate minimum time to reach this station, i.e (from previous
#        station of same line or previous station of other line). Try to reach exit station, while calculating
#        minimum path to reach exit.
#        carAssembleTime(assemTime, transferTime, entryTime, exitTime):
#        n = len(assemTime[0])
#        first = entryTime[0] + assemTime[0][0]
#        second = entryTime[1] + assemTime[1][0]
#        for i in range(1, n):
#           up = min(first + assemTime[0][i],
#                   second + transferTime[1][i] + assemTime[0][i])
#           down = min(second + assemTime[1][i],
#                   first + transferTime[0][i] + assemTime[1][i])
#           first, second = up, down
#        first += exitTime[0], second += exitTime[1]
#        return min(first, second)
# Complexity : O(n)


def carAssembleTime(assemTime, transferTime, entryTime, exitTime):
    n = len(assemTime[0])

    # Time taken to leave first station in line 1
    first = entryTime[0] + assemTime[0][0]

    # Time taken to leave first station in line 2
    second = entryTime[1] + assemTime[1][0]

    for i in range(1, n):
        up = min(first + assemTime[0][i],
                 second + transferTime[1][i] + assemTime[0][i])
        down = min(second + assemTime[1][i],
                   first + transferTime[0][i] + assemTime[1][i])

        first, second = up, down

    first += exitTime[0]
    second += exitTime[1]

    return min(first, second)


if __name__ == "__main__":
    a = [[4, 5, 3, 2], [2, 10, 1, 4]]
    t = [[0, 7, 4, 5], [0, 9, 2, 8]]
    e = [10, 12]
    x = [18, 7]

    print(carAssembleTime(a, t, e, x))
