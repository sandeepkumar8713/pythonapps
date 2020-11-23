# CTCI : Q17_10_Majority_Element
# https://www.geeksforgeeks.org/majority-element/
# Question : Write a function which takes an array and prints the majority element (if it exists), otherwise prints
# "No Majority Element". A majority element in an array A[] of size n is an element that appears more than n/2 times
# (and hence there is at most one such element).
#
# Question Type : Easy
# Used : findCandidate():
#        maj_index = 0, count = 1
#        Run a loop of the input array.
#           If A[maj_index] == A[i]: count++ else count--
#           If count == 0: (take current maj_index)  maj_index = i, count = 1
#        return A[maj_index]
#        This value returned by findCandidate() might be majority number. Run a loop over elements
#        and check if this is majority number.
# Complexity : O(n)


def findCandidate(A):
    maj_index = 0
    count = 1
    for i in range(len(A)):
        if A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index]


def isMajority(A, cand):
    count = 0
    for i in range(len(A)):
        if A[i] == cand:
            count += 1
    if count > len(A) / 2:
        return True
    else:
        return False


def printMajority(A):
    cand = findCandidate(A)

    if isMajority(A, cand):
        print(cand)
    else:
        print("No Majority Element")


if __name__ == "__main__":
    A = [1, 3, 3, 1, 2, 3, 3]
    printMajority(A)

    A = [1, 3, 3, 1, 2, 3]
    printMajority(A)
