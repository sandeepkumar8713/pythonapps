# https://www.geeksforgeeks.org/stepping-numbers/
# Question : Given two integers 'n' and 'm', find all the stepping numbers in range [n, m]. A number is called stepping number
# if all adjacent digits have an absolute difference of 1. 321 is a Stepping Number while 421 is not.
#
# Input : n = 0, m = 21
# Output : 0 1 2 3 4 5 6 7 8 9 10 12 21
#
# Input : n = 10, m = 15
# Output : 10, 12
#
# Question Type : ShouldSee
# Used : Loop for i : 0 to 9 and call recursive function dfs(n, m, i).
#        In dfs(n, m, stepNum). If stepNum is b/w n and m : print stepNum
#        If stepNum == 0 or stepNum >= m: return
#        Get the lastDigit of setNum. From here we can go two ways 1 less of lastDigit or 1 more of lastDigit
#        stepNumA = stepNum * 10 + (lastDigit - 1)
#        stepNumB = stepNum * 10 + (lastDigit + 1)
#        If lastDigit is 0: call dfs only on stepNumB
#        Else If lastDigit is 9: call dfs only on stepNumA
#        Else: call dfs on both stepNumA and stepNumB
# Complexity : O(n)


def dfs(n, m, stepNum):
    if n <= stepNum <= m:
        print(stepNum, end=" ")

    if stepNum == 0 or stepNum >= m:
        return

    lastDigit = stepNum % 10
    # There can be 2 cases either digit to be appended is lastDigit + 1 or lastDigit - 1
    stepNumA = stepNum * 10 + (lastDigit - 1)
    stepNumB = stepNum * 10 + (lastDigit + 1)

    if lastDigit == 0:
        dfs(n, m, stepNumB)
    elif lastDigit == 9:
        dfs(n, m, stepNumA)
    else:
        dfs(n, m, stepNumA)
        dfs(n, m, stepNumB)


def displaySteppingNumbers(n, m):
    for i in range(0, 10):
        dfs(n, m, i)


if __name__ == "__main__":
    n = 0
    m = 21
    displaySteppingNumbers(n, m)
