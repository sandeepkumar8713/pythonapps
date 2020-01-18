# https://www.geeksforgeeks.org/number-of-ways-to-traverse-an-n-ary-tree/
# Question : Given an n-ary tree, count number of ways to traverse an n-ary (or a Directed Acyclic Graph) tree starting
# from the root vertex. The count of all ways to traverse is the product of factorials of the number of children of
# each node.
#
#                 A
#             / /  \  \
#           B  F   D  E
#          / \     |  /|\
#         K  J    G  C H I
#          /\            \
#        N   M            L
#
# 'A' has four children, so 4! permutations possible
# 'B' has two children, so 2! permutations possible
# 'F' has no children, so 0! permutations possible#
#
# Used : Do level order traversal of the n-ary tree. While traversing, calculate the ways by multiplying the factorial
#        of number of children of each node.
#        ways *= factorial(len(temp.children))
# Complexity : O(n * n)
#              We visit each node once during the traversal and take O(n) time to compute factorial for every node.


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


def calculateWays(root):
    ways = 1
    if root is None:
        return 0

    queue = []
    queue.append(root)

    while len(queue) > 0:
        temp = queue.pop(0)

        ways *= factorial(len(temp.children))

        for child in temp.children:
            queue.append(child)

    return ways


if __name__ == "__main__":
    root = Node('A')
    root.children.append(Node('B'))
    root.children.append(Node('F'))
    root.children.append(Node('D'))
    root.children.append(Node('E'))
    root.children[0].children.append(Node('K'))
    root.children[0].children.append(Node('J'))
    root.children[2].children.append(Node('G'))
    root.children[3].children.append(Node('C'))
    root.children[3].children.append(Node('H'))
    root.children[3].children.append(Node('I'))
    root.children[0].children[0].children.append(Node('N'))
    root.children[0].children[0].children.append(Node('M'))
    root.children[3].children[2].children.append(Node('L'))

    print calculateWays(root)
