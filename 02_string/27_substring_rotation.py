# CTCI : Q1_09_String_Rotation
# Question : Assume you have a method isSubString which checks if one word is a substring
# of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one
# call to iSSubString (e.g., "waterbottle" is a rotation of" erbottlewat")
#
# Question Type : Easy
# Used : So, we need to check if there's a way to split s1 into x and y such that xy = s1
#        and yx = s2. Regardless of where the division between x and y is, we can see that
#        yx will always be a substring of xyxy.That is, s2 will always be a substring of s1s1.
# Complexity : O(n^2)


def isSubtring(big, small):
    if big.find(small) >= 0:
        return True
    return False


def isRotation(s1, s2):
    if len(s1) == len(s2) and len(s1) > 0:
        return isSubtring(s1+s1, s2)
    return False


if __name__ == "__main__":
    pairs = [["apple", "pleap"], ["waterbottle", "erbottlewat"], ["camera", "macera"]]
    for pair in pairs:
        print(pair, isRotation(pair[0], pair[1]))
