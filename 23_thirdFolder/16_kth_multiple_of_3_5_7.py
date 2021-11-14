# CTCI : Q17_09_Kth_Multiple
# Question : Design an algorithm to find the kth number such that the only prime factors are
# 3, 5, and 7. Note that 3, 5, and 7 do not have to be factors, but it should not have any
# other prime factors. For example, the first several multiples would be (in order) 1, 3,
# 5, 7, 9, 15, 21.
#
# Question Type : ShouldSee
# Used : 1. x = 0 and queues Q3, QS, and Q7
#        2. Insert 1 into Q3
#        3. Let x be the minimum element in Q3, QS, and Q7. Append x to magic.
#        4. If x was found in:
#           Q3 -> append x*3, x*S and x*7 to Q3, QS, and Q7. Remove x from Q3.
#           QS -> append x*5 and x*7 to QS and Q7. Remove x from QS.
#           Q7 -> only append x*7 to Q7. Remove x from Q7.
#        5. Repeat steps 3 - 4 until we've found k elements.
#        6. Return x
# Complexity : O(n)

import sys


def getHeadElement(queue):
    if len(queue) > 0:
        v = queue[0]
    else:
        v = sys.maxsize
    return v


def getKthMagicNumber(k):
    if k < 0:
        return 0
    val = 0
    queue3 = []
    queue5 = []
    queue7 = []
    queue3.append(1)
    for i in range(0, k):  # Include 0th iteration through kth iteration
        v3 = getHeadElement(queue3)
        v5 = getHeadElement(queue5)
        v7 = getHeadElement(queue7)
        val = min(v7, min(v3, v5))
        # print i, val
        if val == v3:
            queue3.pop(0), queue3.append(3 * val), queue5.append(5 * val), queue7.append(7 * val)
        elif val == v5:
            queue5.pop(0), queue5.append(5 * val), queue7.append(7 * val)
        elif val == v7:
            queue7.pop(0), queue7.append(7 * val)
    return val


if __name__ == "__main__":
    k = 14
    print("kth Element = %s" % getKthMagicNumber(k))
