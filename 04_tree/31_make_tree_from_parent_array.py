# https://www.geeksforgeeks.org/construct-a-binary-tree-from-parent-array-representation/
# Question : Given an array that represents a tree in such a way that array indexes are values in tree nodes and array
# values give the parent node of that particular index (or node). The value of the root node index would always be -1
# as there is no parent for root. Construct the standard linked representation of given Binary Tree from this
# given representation.
#
# Input: parent[] = {1, 5, 5, 2, 2, -1, 3}
# Output: root of below tree
#           5
#         /  \
#        1    2
#       /    / \
#      0    3   4
#          /
#         6
#
# Question Type : Easy
# Used : For the given parent array, convert it into parentChildMap where : key is parentData and value is list of
#        actual values (index). maintain a queue. Insert the root node whose parent is -1.
#        Run a loop while queue is not empty. Pop a node from queue, use its value to fetch its children from the
#           parentChildMap. Make a node out of each child. If node.left is None : node.left = newNode
#           Else: node.right = newNode. And append the newNode to queue.
#        return root
#        Logic :
#        while len(queue) > 0:
#           node = queue.pop(0)
#           parentData = node.data
#           for data in parentChildMap[parentData]:
#               newNode = Node(data)
#               if node.left is None:
#                   node.left = newNode
#               else:
#                   node.right = newNode
#               queue.append(newNode)
#        return root
# Complexity : O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def makeTree(parent):
    parentChildMap = dict()
    for index in range(len(parent)):
        try:
            parentChildMap[parent[index]].append(index)
        except KeyError:
            parentChildMap[parent[index]] = [index]

    queue = []
    # insert the root value
    root = Node(parentChildMap[-1][0])
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        parentData = node.data

        try:
            for data in parentChildMap[parentData]:
                newNode = Node(data)

                if node.left is None:
                    node.left = newNode
                else:
                    node.right = newNode
                queue.append(newNode)
        except KeyError:
            pass

    return root


def printInOrder(node):
    if node is None:
        return
    printInOrder(node.left)
    print(node.data, end=" ")
    printInOrder(node.right)


if __name__ == "__main__":
    # parent = [-1, 0, 0, 1, 1, 3, 5]
    parent = [1, 5, 5, 2, 2, -1, 3]
    root = makeTree(parent)
    printInOrder(root)
    print("")
