# https://www.geeksforgeeks.org/alone-in-couple/
# Question : In a party everyone is in couple except one. People who are in couple have same numbers.
# Find out the person who is not in couple.
#
# Question Type : Generic
# Used : XOR with 1 gives toggles the input
#        XOR with 0 gives back the input
#        XOR operation over same values gives 0. Here same value will cancel out and
#        we will be left with alone
# Complexity : O(n)


def findAlone(arr):
    res = 0
    for item in arr:
        res = res ^ item
    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 2, 1]
    print("Alone:", findAlone(arr))
