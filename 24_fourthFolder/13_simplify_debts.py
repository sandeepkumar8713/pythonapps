# https://www.geeksforgeeks.org/minimize-cash-flow-among-given-set-friends-borrowed-money/
# https://leetcode.com/problems/optimal-account-balancing/
# https://cheonhyangzhang.gitbooks.io/leetcode-solutions/content/solutions-451-500/465-optimal-account-balancing.html
# Question : Given a number of friends who have to give or take some amount of money from one
# another. Design an algorithm by which the total cash flow among all the friends is minimized.
#
# Question Type : ShouldSee
# Used : Make a array of amount[n], it tells the amount to be paid or received
#        Now call recursive function, find max debit and credit.
#        Choose which ever is smaller and add that amount to maxCredit, subtract
#        that amount to maxDebit.
#        So now maxDebit pays minAmount to maxCredit.
#        Call the recursive function again.
#        Logic :  for i in range(n):
#                   for j in range(n):
#                       # toGet(col) - toPay(row)
#                       amount[i] += (graph[j][i] - graph[i][j])
#        def minCashFlowRec(amount):
#           maxCreditIndex = amount.index(max(amount))
#           maxDebitIndex = amount.index(min(amount))
#           if amount[maxCreditIndex] == 0 and amount[maxDebitIndex] == 0: return
#
#           minAmount = min(-amount[maxDebitIndex], amount[maxCreditIndex])
#           amount[maxCreditIndex] -= minAmount, amount[maxDebitIndex] += minAmount
#           print ("maxDebitIndex pays minAmount to maxCreditIndex")
#           minCashFlowRec(amount)
# Complexity : O(n ^ 2)


def minCashFlowRec(amount):
    maxCreditIndex = amount.index(max(amount))
    maxDebitIndex = amount.index(min(amount))

    if amount[maxCreditIndex] == 0 and amount[maxDebitIndex] == 0:
        return

    minAmount = min(-amount[maxDebitIndex], amount[maxCreditIndex])
    amount[maxCreditIndex] -= minAmount
    amount[maxDebitIndex] += minAmount
    print("Person ", maxDebitIndex, " pays ", minAmount, " to ", "Person ", maxCreditIndex)
    minCashFlowRec(amount)


def minCashFlow(graph):
    # Calculate the net amount to be paid or received
    n = len(graph)
    amount = [0] * n
    for i in range(n):
        for j in range(n):
            # toGet(col) - toPay(row)
            amount[i] += (graph[j][i] - graph[i][j])
    minCashFlowRec(amount)


if __name__ == "__main__":
    graph = [[0, 1000, 2000],
             [0, 0, 5000],
             [0, 0, 0]]

    minCashFlow(graph)
