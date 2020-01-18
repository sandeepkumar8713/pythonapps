# https://leetcode.com/problems/distribute-coins-in-binary-tree/solution/
# Question : Given the root of a binary tree with N nodes, each node in the tree has node.val coins,
# and there are N coins total. In one move, we may choose two adjacent nodes and move one coin from
# one node to another. (The move may be from parent to child, or from child to parent.)
# Return the number of moves required to make every node have exactly one coin.
#
# Used : dfs, We need to take care do distribute excess coins, it can be negative to, if needed.
#        Let dfs(node) be the excess number of coins in the subtree at or below this node: namely, the number of
#        coins in the subtree, minus the number of nodes in the subtree. Then, the number of moves we make from
#        this node to and from its children is abs(dfs(node.left)) + abs(dfs(node.right)). After, we have an
#        excess of node.val + dfs(node.left) + dfs(node.right) - 1 coins at this node.
#        Logic : def dfs(node, ans):
#        if node is None: return 0
#        L, R = dfs(node.left, ans), dfs(node.right, ans)
#        ans[0] += abs(L) + abs(R)
#        return node.data + L + R - 1
#        Remember : Answer is ans[0]
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def dfs(node, ans):
    if node is None:
        return 0

    L, R = dfs(node.left, ans), dfs(node.right, ans)
    ans[0] += abs(L) + abs(R)
    return node.data + L + R - 1


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(0)
    root.right = Node(0)

    ans = [0]
    dfs(root, ans)
    print ans[0]

