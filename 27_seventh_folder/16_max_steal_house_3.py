# https://leetcode.com/problems/house-robber-iii/
# Question : The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called root. Besides the root, each house has one and only
# one parent house. After a tour, the smart thief realized that all houses in this place
# form a binary tree. It will automatically contact the police if two directly-linked houses
# were broken into on the same night. Given the root of the binary tree, return the maximum
# amount of money the thief can rob without alerting the police.
# Similar : 21_firstFolder/21_max_steal_house.py
#
# Question Type : Generic, SimilarAdded
# Used : Given input is in level order traversal, do BFS to convert it to tree.
#        Do DFS over the given tree (post order traversal). Each level should return 2 levels
#        results. We should choose max of 2 levels return max as ans1 and next level as ans2.
#        Logic :
#        def dfs(root):
#        if not root: return 0, 0
#        l1, l2 = dfs(root.left)
#        r1, r2 = dfs(root.right)
#        ans1 = max(l1 + r1, l2 + r2 + root.val)
#        ans2 = l1 + r1
#        return ans1, ans2
#
#        ans1, ans2 = dfs(root)
#        return max(ans1, ans2)
# Complexity : O(n)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrderToTree(inpArr):
    n = len(inpArr)
    root = Node(inpArr[0])
    queue = [root]
    i = 1

    while queue:
        levelLen = len(queue)
        while levelLen > 0:
            rootNode = queue.pop(0)
            levelLen -= 1

            if i < n and inpArr[i] is not None:
                leftNode = Node(inpArr[i])
                queue.append(leftNode)
            else:
                leftNode = None

            if i + 1 < n and inpArr[i + 1] is not None:
                rightNode = Node(inpArr[i + 1])
                queue.append(rightNode)
            else:
                rightNode = None

            rootNode.left = leftNode
            rootNode.right = rightNode
            i += 2

    return root


def dfs(root):
    if not root:
        return 0, 0

    l1, l2 = dfs(root.left)
    r1, r2 = dfs(root.right)

    ans1 = max(l1 + r1, l2 + r2 + root.val)
    ans2 = l1 + r1

    return ans1, ans2


def rob(inpArr):
    root = levelOrderToTree(inpArr)
    ans1, ans2 = dfs(root)
    return max(ans1, ans2)


if __name__ == "__main__":
    inpArr = [3, 2, 3, None, 3, None, 1]
    print(rob(inpArr))

    inpArr = [3, 4, 5, 1, 3, None, 1]
    print(rob(inpArr))

