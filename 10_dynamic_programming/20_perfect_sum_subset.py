# https://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
# Question : Given an array of integers and a sum, the task is to print all subsets of given array with
# sum equal to given sum.
#
# Examples:
# Input : arr[] = {2, 3, 5, 6, 8, 10}
#         sum = 10
# Output : 5 2 3
#          2 8
#          10
#
# Question Type : Generic
# Used : Make a matrix dp : size n * (1+targetSum), such that dp[i][j] stores true if sum j
#        is possible with array elements from 0 to i.
#        Logic :
#        Make a first column of dp True, for sum 0
#        In first row, if sum is arr[i] set True.  (if inpArr[0] <= targetSum: dp[0][inpArr[0]] = True)
#           Then run 2 loops for i : 1 to n, j : 0 to (target+1)
#               if inpArr[i] <= j:
#               (If this element is included, check if (j-inpArr[i]) can be achieved with i-1 elements)
#                   dp[i][j] = dp[i-1][j] or dp[i-1][j-inpArr[i]]
#               else: dp[i][j] = dp[i - 1][j]
#        if dp[n-1][targetSum] is False: print "No subset possible"
#        printSubsetsRec(dp, inpArr, n-1, targetSum, [])
#        Now we call a recursive function which picks and ignores the current element and check if the target can
#        achieved, i.e. at the end sum becomes 0, print the elements selected so far.
#        printSubsetsRec(dp, inpArr, i, targetSum, subArray):
#        if i == 0 and targetSum != 0 and dp[0][targetSum]:
#           subArray.append(inpArr[i]), targetSum = 0
#        if i == 0 and targetSum == 0:
#           print (subArray), del subArray[:], return
#        if dp[i - 1][targetSum]: (excluding)
#           subArrayB = subArray[:], printSubsetsRec(dp, inpArr, i - 1, targetSum, subArrayB)
#        if targetSum >= inpArr[i] and dp[i-1][targetSum-inpArr[i]]: (including)
#           subArray.append(inpArr[i]), printSubsetsRec(dp, inpArr, i - 1, targetSum-inpArr[i], subArray)
# Complexity : O(n * targetSum)


def printSubsetsRec(dp, inpArr, i, targetSum, subArray):
    if i == 0 and targetSum != 0 and dp[0][targetSum]:
        subArray.append(inpArr[i])
        targetSum = 0

    if i == 0 and targetSum == 0:
        print(subArray)
        del subArray[:]
        return

    # If given sum can be achieved after ignoring current element
    if dp[i - 1][targetSum]:
        subArrayB = subArray[:]
        printSubsetsRec(dp, inpArr, i - 1, targetSum, subArrayB)

    # If given sum can be achieved after considering current element
    if targetSum >= inpArr[i] and dp[i-1][targetSum-inpArr[i]]:
        subArray.append(inpArr[i])
        printSubsetsRec(dp, inpArr, i - 1, targetSum-inpArr[i], subArray)


def printAllSubsets(inpArr, targetSum):
    n = len(inpArr)
    if n == 0 and targetSum < 0:
        return

    dp = []
    for i in range(n):
        dp.append([False] * (targetSum + 1))

    # Sum 0 can always be achieved with 0 elements
    for i in range(n):
        dp[i][0] = True

    # Sum arr[0] can be achieved with single element
    if inpArr[0] <= targetSum:
        dp[0][inpArr[0]] = True

    for i in range(1, n):
        for j in range(targetSum+1):
            if inpArr[i] <= j:
                # If this element is included, check if (j-inpArr[i]) can be achieved with i-1 elements
                dp[i][j] = dp[i-1][j] or dp[i-1][j-inpArr[i]]
            else:
                dp[i][j] = dp[i - 1][j]

    if dp[n-1][targetSum] is False:
        print("No subset possible")
        return
    printSubsetsRec(dp, inpArr, n-1, targetSum, [])


if __name__ == "__main__":
    inpArr = [1, 2, 3, 4, 5]
    targetSum = 10
    printAllSubsets(inpArr, targetSum)
