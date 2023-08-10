# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Similar : https://leetcode.com/problems/unique-binary-search-trees/
# Question : Given an integer n, return all the structurally unique BST's (binary search trees), which
# has exactly n nodes of unique values from 1 to n. Return the answer in any order.
# (countBST(n)) = Catalan number Cn = (2n)!/(n+1)!*n! = O( (4^n) / (n * (n)^0.5) )
#
# Question type : Generic, Similar added
# Used : We will run a loop for i start to end. Take this a root node.
#        Now call recursive function of start, i - 1 and i + 1, end
#        The resursive function will return list of subtress, we will make all possible combination
#        of left and right subtree.
# Logic: def generate_trees(start, end):
#        if start > end: return [None, ]
#        all_trees = []
#        for i in range(start, end + 1):
#           left_trees = generate_trees(start, i - 1)
#           right_trees = generate_trees(i + 1, end)
#           for l in left_trees:
#               for r in right_trees:
#                 current_tree = TreeNode(i)
#                 current_tree.left = l
#                 current_tree.right = r
#                 all_trees.append(current_tree)
#        return all_trees
# Complexity : Catalan number (Cn)

class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        # Pre order
        if self.left is None and self.right is None:
            return str(self.value)
        return str(self.value) + " " + str(self.left) + " " + str(self.right)


def generate_trees(start, end):
    if start > end:
        return [None, ]

    all_trees = []
    for i in range(start, end + 1):
        left_trees = generate_trees(start, i - 1)
        right_trees = generate_trees(i + 1, end)

        # This is returning list of subtress, we will make all possible combination of left and right subtree.
        for l in left_trees:
            for r in right_trees:
                current_tree = TreeNode(i)
                current_tree.left = l
                current_tree.right = r
                all_trees.append(current_tree)

    return all_trees


def get_all_trees(n):
    if n == 0:
        return []
    tree_list = generate_trees(1, n)
    result = []
    for tree in tree_list:
        result.append(str(tree))

    return result


if __name__ == "__main__":
    result = get_all_trees(3)
    print(result)
