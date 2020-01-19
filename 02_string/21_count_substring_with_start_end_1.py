# https://www.geeksforgeeks.org/given-binary-string-count-number-substrings-start-end-1/
# Question : Given a binary string, count number of substrings that start and end with 1.
#
# For example, if the input string is "00100101", then there are three substrings "1001", "100101" and "101".
#
# Question Type : Easy
# Used : a) Count the number of 1's. Let the count of 1's be m.
#        b) Return m(m-1)/2
#        The idea is to count total number of possible pairs of 1's.
# Complexity : O(n)


def countSubStr(inpStr):
    onesCount = 0

    for ch in inpStr:
        if ch == '1':
            onesCount += 1

    return onesCount * (onesCount - 1) // 2


if __name__ == "__main__":
    inpStr = "00100101"
    print(countSubStr(inpStr))
