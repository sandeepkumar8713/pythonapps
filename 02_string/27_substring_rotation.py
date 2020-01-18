# CTCI : Q1_09_String_Rotation
# Question : Assume you have a method i 5Su b 5 tr ing which checks if one word is a substring
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
# call to i5Sub5tring (e.g., "waterbottle" is a rotation of" erbottlewat")
#
# Used : So, we need to check if there's a way to split s1 into x and y such that xy = s1 and yx = s2. Regardless of
# where the division between x and y is, we can see thatyx will always be a substring of xyxy.That is, s2 will
# always be a substring of s1s1.
# Complexity : O(n^2)


def isSubtring(big,small):
    if big.find(small) >= 0:
        return True
    return False


def isRotation(s1,s2):
    if len(s1) == len(s2) and len(s1) > 0:
        return isSubtring(s1+s1, s2)
    return False


if __name__ == "__main__":
    pairs = [["apple", "pleap"], ["waterbottle", "erbottlewat"], ["camera", "macera"]]
    for pair in pairs:
        print (pair, isRotation(pair[0],pair[1]))
