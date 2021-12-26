# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
# Question : We have n chips, where the position of the ith chip is position[i].
# We need to move all the chips to the same position. In one step, we can change the position
# of the ith chip from position[i] to:
# position[i] + 2 or position[i] - 2 with cost = 0.
# position[i] + 1 or position[i] - 1 with cost = 1.
# Return the minimum cost needed to move all the chips to the same position.
# Follow-up: Find a final position which requries minimum number of moves to get
# all chips to that position in minimum cost.
#
# Question Type : Easy
# Used : Move all the coins at even places together.
#        Similarly move all the coins at odd places together.
#        Now only cost is to move all the odd and even coins together.
#        Find min of above.
#        For followup question : To get the final position, first find
#        the median of all elements in P.
#        If the parity of median (odd or even) is same as parity of positions
#        giving min cost, then final position is the median itself.
#        Otherwise, the final position should be median ± 1
# Complexity : O(n)


def minCostToMoveChips(inpArr):
    pos = [0, 0]
    for ele in inpArr:
        pos[ele & 1] += 1
    return min(pos)


if __name__ == "__main__":
    position = [2, 2, 2, 3, 3]
    print (minCostToMoveChips(position))
