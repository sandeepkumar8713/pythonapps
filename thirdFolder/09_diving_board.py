# CTCI : Q16_11_Diving_Board
# Question : You are building a diving board by placing a bunch of planks of wood end-to-end.
# There are two types of planks, one of length shorter and one of length longer. You must use
# exactly K planks of wood. Write a method to generate all possible lengths for the diving board.
#
# Used : We know that k is constant and (smallCount + largerCount) == k. So we will try all combinations of
#        smallCount and largerCount and save corresponding length in list
#        for smallCount in range(k+1):
#           largerCount = k - smallCount
#           length = smallCount * smallerBoard + largerCount * largerBoard
#           lengths.append(length)
# Complexity : O(k)


def allLengths(k, smallerBoard, largerBoard):
    lengths = []
    for smallCount in range(k+1):
        largerCount = k - smallCount
        length = smallCount * smallerBoard + largerCount * largerBoard
        lengths.append(length)
    return lengths


if __name__ == "__main__":
    k = 12
    smallerBoard = 1
    largerBoard = 3
    print (allLengths(k, smallerBoard, largerBoard))
