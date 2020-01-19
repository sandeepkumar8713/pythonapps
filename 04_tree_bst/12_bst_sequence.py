# CTCI : Q4_09_BST_Sequences
# https://hackernoon.com/bst-sequences-in-python-c072c0e9b19f
# Question : A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.
#
# TODO :: go through the code and the one in java, add used explaination
#

import copy

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._insert(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._insert(val, node.r)
            else:
                node.r = Node(val)

# 'first' list shall be referred to as first[]
# 'second' list shall be referred to as second[]
# 'prefix' list shall be referred to as prefix[]
def weaveLists(first, second, results, prefix):
    # if first or second is an empty list
    if not first or not second:
        # ensuring that result is a CLONE and not a reference to prefix
        result = copy.deepcopy(prefix) ### EDIT HERE TO DEEPCOPY
        # add result to first or/ and second lists
        if first:
            result += first
        if second:
            result += second
        # append the weaved list which is result, to results
        results.append(result)
        return
        # add result to first or/ and second lists
        if first:
            result += first
        if second:
            result += second
        # append the weaved list which is result, to results
        results.append(result)
        return
    # this would be the method as described in the textbook
    # first, remove and store first element of first[]
    headFirst = first.pop(0)
    # append to prefix
    prefix.append(headFirst)
    ### add recursive call to operate on first[]
    weaveLists(first, second, results, prefix)
    # exit when first[] is empty
    # reset prefix for second recursive call below by removing last element
    # IMPT to modify in-place
    del prefix[-1]
    # reset first[] for second recursive call below by adding back first element
    # IMPT to modify in-place
    first.insert(0,headFirst)
    # do the same thing on the second[]
    headSecond = second.pop(0)
    prefix.append(headSecond)
    ### add recursive call to operate on first[] and second[]
    weaveLists(first, second, results, prefix)
    del prefix[-1]
    second.insert(0,headSecond)


def allSequences(node):
    # this is the final list of lists we want to output
    results = []
    # termination, append [] so that results will not be empty\
    # and the nested for loop will still execute since
    # leftSeq == [[]] and rightSeq == [[]] in termination
    if not node:
        results.append([])
        return results
    # prefix will always be root of subtree
    prefix = []
    prefix.append(node.v)
    # then represent the left and right subtrees
    leftSeq = allSequences(node.l)
    rightSeq = allSequences(node.r)
    # nested for loop and call weaveLists on each list in
    # leftSeq and rightSeq, which are list of lists
    # and each represents results of each subtree
    for left in leftSeq:
        for right in rightSeq:
            # make weaved an empty list,
            # which is results in weaveList
            weaved = []
            weaveLists(left, right, weaved, prefix)
            # weaved is list of lists generated by left[] and right[]
            # add weaved list of lists to final
            # results list of lists
            results += weaved
    return results


if __name__ == "__main__":
    tree = Tree()

    tree.insert(20)
    tree.insert(10)
    tree.insert(25)
    tree.insert(5)
    tree.insert(15)
    allSeq = allSequences(tree.getRoot())
    for each in allSeq:
        print (each)
    print (len(allSeq))