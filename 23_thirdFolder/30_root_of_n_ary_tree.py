# https://leetcode.com/discuss/interview-question/351946/Google-or-Onsite-or-Find-Root-of-N-ary-Tree
# Question : Given an N-ary tree as a list of nodes Node[] tree. Each node has a unique value.
# In graph theory, an m-ary tree (also known as k-ary or k-way tree) is a rooted tree in which each
# node has no more than m children. A binary tree is the special case where m = 2, and a ternary
# tree is another case with m = 3 that limits its children
# to three.
#
# Question Type : ShouldSee
# Used : Loop over the input nodes and its children. While doing so, keeping XORing the values
#        to a temp val. After the loop, each element will be visited twice accept the root node.
#        So temp value will be root value.
#        Logic : def findRoot(nodes):
#        rootVal = 0
#        for node in nodes:
#           rootVal ^= node.val
#           for child in node.children:
#               rootVal ^= child.val
#        for node in nodes:
#           if rootVal == node.val: return node
#        return None
# Complexity : O(n)


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


def findRoot(nodes):
    rootVal = 0
    for node in nodes:
        rootVal ^= node.data
        for child in node.children:
            rootVal ^= child.data

    for node in nodes:
        if rootVal == node.data:
            return node

    return None


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.children.append(n2)
    n1.children.append(n3)
    n1.children.append(n4)

    root = findRoot([n2, n3, n4, n1])
    if root:
        print(root.val)
