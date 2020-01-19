# Question : Given a string s we need to tell minimum characters to be appended (insertion at end) to make a
# string palindrome.
#
# Input : s = "abede"
# Output : 2
# We can make string palindrome as "abedeba" by adding ba at the end of the string.
#
# Question Type : ShouldSee
# Used : Remove characters from the beginning of the string one by one and check if the string is palindrome or not.
#        If true the output becomes the number of characters removed from the string.
# Complexity : O(n ^ 2)


def isPlaindrome(inpStr):
    left = 0
    right = len(inpStr) - 1
    s = 0
    while left <= right:
        if inpStr[left] != inpStr[right]:
            return False
        left += 1
        right -= 1
    return True


def getAppendCount(inpStr):
    appendCount = 0
    for i in range(0, len(inpStr)):
        if isPlaindrome(inpStr[i:]):
            return appendCount
        else:
            appendCount += 1
    return appendCount


if __name__ == "__main__":
    inpStr = "madam1"
    print(getAppendCount(inpStr))
