# https://leetcode.com/problems/flip-game-ii/
# https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/294.html
# Question : You are playing the following Flip Game with your friend: Given a string that contains
# only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--".
# The game ends when a person can no longer make a move and therefore the other person will be the winner.
# Write a function to determine if the starting player can guarantee a win.
# For example, given s = "++++", return true. The starting player can guarantee a win by flipping
# the middle "++" to become "+--+".
#
# Question Type : Generic
# Used : We will use DP with DFS
#        Here DP[(left,right)] represent if the first player can win for element in input arr, b/w left and right.
#        Run a loop over input array. If we find ++, call DFS of remaining left and right side.
#        If both of them return False, Then current player can win so return True.
#        Keep saving intermediate result in memory table.
# Logic: def can_win_util(memo_dict, left, right):
#        if left >= right: return False
#        res = memo_dict.get((left, right), None)
#        if res is not None: return None
#        res = False
#        for i in range(left, right):
#           if inpStr[i] == "+" and inpStr[i + 1] == "+":
#               left_side = can_win_util(memo_dict, left, i - 1)
#               right_side = can_win_util(memo_dict, i + 1, right)
#               if not left_side and not right_side:
#                   res = True
#                   break
#        memo_dict[(left, right)] = res
#        return res
#
#        memo_dict = dict()
#        return can_win_util(memo_dict, 0, n - 1)
# Complexity : O(n^2)

def can_win_util(memo_dict, left, right):
    if left >= right:
        return False

    res = memo_dict.get((left, right), None)
    if res is not None:
        return None

    res = False
    for i in range(left, right):
        if inpStr[i] == "+" and inpStr[i + 1] == "+":
            left_side = can_win_util(memo_dict, left, i - 1)
            right_side = can_win_util(memo_dict, i + 1, right)
            if not left_side and not right_side:
                res = True
                break

    memo_dict[(left, right)] = res
    return res


def can_win(inpStr):
    n = len(inpStr)
    memo_dict = dict()
    return can_win_util(memo_dict, 0, n - 1)


if __name__ == "__main__":
    inpStr = "++++"
    print(can_win(inpStr))

    inpStr = "+--++--+"
    print(can_win(inpStr))

    inpStr = "+--------+"
    print(can_win(inpStr))
