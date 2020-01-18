# Question : Given N activities with their start and finish times. Select the maximum number of activities that can be performed by
# a single person, assuming that a person can only work on a single activity at a time.
#
# Used : Given two array start and finish. Sort the finish array and accordingly sort the start array.
#        Mark the first task as done, now run a loop over remaining tasks.
#        If this tasks start time is more than previous done task's finish time then mark this as done and update this
#           task as previous done task.
# Complexity : O(n log n)


def printMaxActivities(s, f):
    n = len(f)
    print "The following activities are selected"

    sortedStart = [x for _, x in sorted(zip(f, s))]
    sortedFinish = sorted(f)

    # The first activity is always selected
    # i denotes recently selected job
    i = 0
    print sortedStart[i], sortedFinish[i]

    # Consider rest of the activities
    for j in xrange(n):
        if sortedStart[j] >= sortedFinish[i]:
            print sortedStart[j], sortedFinish[j]
            i = j


if __name__ == "__main__":
    # start = [1, 3, 0, 5, 8, 5]
    # finish = [2, 4, 6, 7, 9, 9]
    start = [5, 1, 3, 0, 5, 8]
    finish = [9, 2, 4, 6, 7, 9]
    # start = [5, 15, 27, 50]
    # finish = [24, 25, 40, 60]
    printMaxActivities(start, finish)
