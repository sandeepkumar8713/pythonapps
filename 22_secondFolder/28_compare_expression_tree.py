# https://leetcode.com/discuss/interview-question/339111/Google-or-Onsite-or-Compare-Expression-Trees
# Question : Given 2 binary expression trees tree1 and tree2. The leaves of a binary
# expression tree are variable names and the other nodes contain operators. Find out if the
# expressions represented by these trees are equal or not. There are only plus signs + and
# letters in the tree. Input is guaranteed to be valid. Follow up : let us
# (-) operator is also added.
#
# Example : Input:
# 	 tree1
# 	   +
# 	 /   \
# 	a     b
#
# 	 tree2
# 	   +
# 	 /   \
# 	b     a
# Output: true
# Explanation: a + b = b + a
#
# Question Type : Generic
# Used : Do in-order traversal. While doing so, if operator is + or *,
#        check if left and right of roots are equal.
#        Else check if left, left and right, right of roots are equal.
#        Logic : def isEqual(root1, root2):
#        if root1 is None and root2 is None: return True
#        if root1 is None or root2 is None: return False
#        equals = False
#        if root1.val == '+' or root1.val == '*':
#           equals = root1.val == root2.val and isEqual(root1.left, root2.right) and isEqual(root1.right, root2.left)
#        return equals or
#           (root1.val == root2.val and isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right))
# Complexity : O(n)


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def isEqual(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    equals = False
    if root1.val == '+' or root1.val == '*':
        equals = root1.val == root2.val and isEqual(root1.left, root2.right) and isEqual(root1.right, root2.left)

    return equals or (root1.val == root2.val and isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right))


if __name__ == "__main__":
    root1 = Node('+')
    root1.left = Node('a')
    root1.right = Node('b')

    root2 = Node('+')
    root2.left = Node('b')
    root2.right = Node('a')

    print(isEqual(root1, root2))

    root1 = Node('-')
    root1.left = Node('a')
    root1.right = Node('b')

    root2 = Node('-')
    root2.left = Node('b')
    root2.right = Node('a')

    print(isEqual(root1, root2))
