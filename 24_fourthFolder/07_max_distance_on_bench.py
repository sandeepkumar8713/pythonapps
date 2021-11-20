# https://www.careercup.com/question?id=5385816814125056
# https://leetcode.com/problems/maximize-distance-to-closest-person/
# Question : Given a bench with n seats and few people sitting, tell the seat number each time when a new person
# goes to sit on the bench such that his distance from others is maximum.
#
# Question Type : Generic
# Used : We will use max heap. Make a class with 2 member, leftEdge and rightEdge,
#        these tell the left and right distance from current seat to previous seat.
#        If the bench is empty place it on first index. Next time place it at last index.
#        Now make a seat(0,n-1) and insert in max heap.
#        When next person comes in,
#        When next person comes in, pop top element from the max heap, result will be
#        (left+right)/2 of popped element.
#        Insert 2 nodes : seat(left,(left+right)/2) and seat((left+right)/2,right) in max
#        heap and heapify.
#        Please note that we are inserting range in heap. So that we can place the next
#        person in middle of the range.
#        Comparison of max heap would be difference between left and right. So the top
#        element has max range, between which next person will be placed.
#        Logic:
#        def getSeat(inpArr, seatingSpaces):
#        n = len(inpArr)
#        if inpArr[0] == 0:
#           inpArr[0] = 1, return 0
#        if inpArr[n-1] == 0:
#           seatingSpaces.append(Seat(0, n-1)), inpArr[n-1] = 1
#           return n-1
#        seatingSpacesSorted = sorted(seatingSpaces,  key=functools.cmp_to_key(compare))
#        copyToOriginal(seatingSpacesSorted, seatingSpaces)
#        currentSeat = seatingSpaces.pop(0)
#        seatingSpaces.append(Seat(currentSeat.leftEdge, (currentSeat.leftEdge + currentSeat.rightEdge) // 2))
#        seatingSpaces.append(Seat((currentSeat.leftEdge + currentSeat.rightEdge) // 2, currentSeat.rightEdge))
#        newSeat = (currentSeat.leftEdge + currentSeat.rightEdge) // 2
#        inpArr[newSeat] = 1
#        return newSeat
# Complexity : Build Heap: O(N)
#              Return next seat: O(1) --> getMax operation
#              Add entries to heap: O(logN)

import functools

class Seat:
    def __init__(self, leftEdge, rightEdge):
        self.leftEdge = leftEdge
        self.rightEdge = rightEdge


def compare(seat1, seat2):
    seat2Diff = seat2.rightEdge - seat2.leftEdge
    seat1Diff = seat1.rightEdge - seat1.leftEdge
    if seat1Diff == seat2Diff:
        return 0
    if seat2Diff < seat1Diff:
        return -1
    else:
        return 1


def copyToOriginal(seatingSpacesSorted, seatingSpaces):
    for i in range(len(seatingSpacesSorted)):
        seatingSpaces[i] = seatingSpacesSorted[i]


def getSeat(inpArr, seatingSpaces):
    n = len(inpArr)
    if inpArr[0] == 0:
        inpArr[0] = 1
        return 0
    if inpArr[n-1] == 0:
        seatingSpaces.append(Seat(0, n-1))
        inpArr[n-1] = 1
        return n-1

    # sort in descending order of difference
    seatingSpacesSorted = sorted(seatingSpaces,  key=functools.cmp_to_key(compare))
    copyToOriginal(seatingSpacesSorted, seatingSpaces)

    currentSeat = seatingSpaces.pop(0)
    seatingSpaces.append(Seat(currentSeat.leftEdge, (currentSeat.leftEdge + currentSeat.rightEdge) // 2))
    seatingSpaces.append(Seat((currentSeat.leftEdge + currentSeat.rightEdge) // 2, currentSeat.rightEdge))
    newSeat = (currentSeat.leftEdge + currentSeat.rightEdge) // 2
    inpArr[newSeat] = 1
    return newSeat


if __name__ == "__main__":
    n = 10
    inpArr = [0] * n
    seatingSpaces = []
    for i in range(n):
        print("Next seat : %s" % getSeat(inpArr, seatingSpaces))
