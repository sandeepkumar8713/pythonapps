# CTCI : Q8_04_Power_Set
# https://www.geeksforgeeks.org/find-distinct-subsets-given-set/
# Question : Given a set of positive integers, find all its subsets. The set can contain duplicate elements,
# so any repeated subset should be considered only once in the output.
#
# Input:  S = {1, 2, 2}
# Output:  {}, {1}, {2}, {1, 2}, {2, 2}, {1, 2, 2}
#
# Question Type : ShouldSee
# Used : Call a recursive function printPowerSetUtil(inpArr, i, subSet, powerSet) with input
#        printPowerSetUtil(inpArr, 0, [], powerSet). if i == len(inpArr): powerSet.append(subSet[::]) and return
#           Call printPowerSetUtil() again 2 times, once by ignoring this element and other by including this element.
#           subSet.pop()
#       PowerSet has all the possible subset but it might contain duplicate subset. Run a 2 loops to find distinct
#       subset and print them.
# Complexity : O(2 ^ n * 2 ^ n * 2 ^ n) so O(2 ^ (3n))


def cmp(a, b):
    return (a > b) - (a < b)


def printPowerSetUtil(inpArr, i, subSet, powerSet):
    if i == len(inpArr):
        powerSet.append(subSet[::])
        return

    # ignore
    printPowerSetUtil(inpArr, i + 1, subSet, powerSet)
    subSet.append(inpArr[i])
    # include
    printPowerSetUtil(inpArr, i + 1, subSet, powerSet)
    subSet.pop()


def printPowerSet(inpArr):
    powerSet = []
    printPowerSetUtil(inpArr, 0, [], powerSet)
    distinctList = []
    for subSet in powerSet:
        alreadyPresent = False
        for distSet in distinctList:
            res = cmp(subSet, distSet)
            if res == 0:
                alreadyPresent = True
        if not alreadyPresent:
            distinctList.append(subSet)

    for subSet in distinctList:
        print(subSet)


if __name__ == "__main__":
    inpArr = [10, 11, 12, 13]
    # inpArr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    printPowerSet(inpArr)
