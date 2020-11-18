# https://careercup.com/question?id=5090913987067904
# Question : Display nodes of a tree in level order using DFS
#
#                       20
#                     /    \
#                   8       22
#                 /   \    /  \
#               5      3  4   25
#                     / \
#                   10    14
#
# Question Type : ShouldSee
# Used : Do pre-order traversal while calculating level for each node and adding the elements in map using level.
#        After traversal, sort the map using keys and print the values
#        def getLevelDFS(root, level, m):
#        if root is None: return
#        try:
#           m[level].append(root.data)
#        except:
#           m[level] = [root.data]
#
#        getLevelDFS(root.left, level + 1, m)
#        getLevelDFS(root.right, level + 1, m)
# Complexity : O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLevelDFS(root, level, m):
    if root is None:
        return

    try:
        m[level].append(root.data)
    except:
        m[level] = [root.data]

    getLevelDFS(root.left, level + 1, m)
    getLevelDFS(root.right, level + 1, m)


def levelOrder(root):
    m = dict()
    hd = 0
    getLevelDFS(root, hd, m)

    for key in sorted(m):
        for item in m[key]:
            print(item, end=" ")
        print("")


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    levelOrder(root)
