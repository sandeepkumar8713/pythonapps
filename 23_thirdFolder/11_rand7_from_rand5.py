# CTCI : Q16_23_Rand7_From_Rand5
# Question : Implement a method rand7 () given rand S (). That is, given a method that
# generates a random number between O and 4 (inclusive), write a method that generates a random
# number between O and 6 (inclusive).
#
# Used : We just need to generate a range of values where each value is equally likely
#       (and where the range has at least seven elements). If we can do this, then we
#       can discard the elements greater than 7.
#       Do r1 = 2 * rand5(), Here r1 will always be even, to make it odd do,
#       r2 = rand5() if r2 != 4: rand1 = r2 % 2, num = r1 + rand1
#       return num if it less than 7 else keep looping
# Complexity : non deterministic number of calls

import random


def rand5():
    return int(random.random() * 100) % 5


def rand7():
    while True:
        r1 = 2 * rand5()
        r2 = rand5()
        if r2 != 4:     # Has extra even num-discard the extra
            rand1 = r2 % 2
            num = r1 + rand1
            if num < 7:
                return num


if __name__ == "__main__":
    testSize = 1000000
    arr = [0] * 7
    for i in range(testSize):
        arr[rand7()] += 1

    for i in range(len(arr)):
        percent = 100.0 * arr[i] / testSize
        print ("%s appeared %s percent of the time." % (i, percent))
