# Question : Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the
# number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n. Initially, the first player
# names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first
# player colors the node with value x red, and the second player colors the node with value y blue. Then, the players
# take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player
# 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child,
# or parent of the chosen node.) If (and only if) a player cannot choose such a node in this way, they must pass
# their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.
# You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.
# If it is not possible, return false.
# Followup : If player A takes the first hand instead, which node should he pick, so that it always wins.
#
# Used : To check if second player can win. Call a recursive function to get, left and right subtree count from the node
#        selected by the first player. It also returns total number of nodes from given root. Now find max of left
#        subtree, right subtree and remaining nodes(parent). If this max is more than n/2 return true.
#        Logic : def btreeGameWinningMoveSecondPlayer(root, x):
#        totalNodes = count(root, x, leftSubtree, rightSubtree)
#        parentNodes = totalNodes - leftSubtree[0] - rightSubtree[0] - 1
#        maxSide = max(leftSubtree[0], rightSubtree[0])
#        maxSide = max(maxSide, parentNodes)
#        return maxSide > (totalNodes // 2)
#        To find node for first player, so that he always wins: do post-order traversal of the tree. While doing so,
#        find a node at which, any 2 subtree count is more than other subtree count. So when second player chooses
#        any subtree, it will always loose.
#        Logic : def countMax(root, n, ans):
#        if root is None or ans[0] > 0: return 0
#        leftSubtree = countMax(root.left, n, ans)
#        rightSubtree = countMax(root.right, n, ans)
#        parentSubtree = n - leftSubtree - rightSubtree - 1
#        if parentSubtree < (leftSubtree + rightSubtree) and
#           leftSubtree < (parentSubtree + rightSubtree) and
#           rightSubtree < (parentSubtree + leftSubtree):
#               ans[0] = root.val
#        return leftSubtree + rightSubtree + 1
# Complexity : O(n)


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def btreeGameWinningMoveSecondPlayer(root, x):
    leftSubtree = [0]
    rightSubtree = [0]
    totalNodes = count(root, x, leftSubtree, rightSubtree)
    parentNodes = totalNodes - leftSubtree[0] - rightSubtree[0] - 1
    maxSide = max(leftSubtree[0], rightSubtree[0])
    maxSide = max(maxSide, parentNodes)

    return maxSide > (totalNodes // 2)


def count(root, x, leftSubtree, rightSubtree):
    if root is None:
        return 0
    l = count(root.left, x, leftSubtree, rightSubtree)
    r = count(root.right, x, leftSubtree, rightSubtree)

    if root.val == x:
        leftSubtree[0] = l
        rightSubtree[0] = r

    return l + r + 1


def countMax(root, n, ans):
    if root is None or ans[0] > 0:
        return 0

    leftSubtree = countMax(root.left, n, ans)
    rightSubtree = countMax(root.right, n, ans)
    parentSubtree = n - leftSubtree - rightSubtree - 1

    if parentSubtree < (leftSubtree + rightSubtree) and leftSubtree < (parentSubtree + rightSubtree) and \
            rightSubtree < (parentSubtree + leftSubtree):
        ans[0] = root.val

    return leftSubtree + rightSubtree + 1


def btreeGameWinningMoveFirstPlayer(root, n):
    ans = [-1]
    countMax(root, n, ans)
    if ans[0] > 0:
        return ans[0]
    else:
        return None


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left = Node(6)
    root.right.right = Node(7)

    x = 3
    n = 11
    print btreeGameWinningMoveSecondPlayer(root, x)
    print btreeGameWinningMoveFirstPlayer(root, n)
