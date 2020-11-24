# https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
# Question : Serialization is to store tree in a file so that it can be later restored. The structure of tree
# must be maintained. Deserialization is reading tree back from file.
#
# Question Type : ShouldSee
# Used : def serialize(root, fp):
#        if root is None:
#           fp.write(str(MARKER) + " ")
#           return
#        fp.write(str(root.data) + " ")
#        serialize(root.left, fp)
#        serialize(root.right, fp)
#
#        def deSerialize(numList):
#        if len(numList) is 0: return None
#        element = numList.pop(0)
#        if element is MARKER: return None
#        root = Node(element)
#        root.left = deSerialize(numList)
#        root.right = deSerialize(numList)
#        return root
# Complexity : O(n)

MARKER = -1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root, result):
    if root is None:
        return
    inorder(root.left, result)
    result.append(root.data)
    inorder(root.right, result)


def serialize(root, fp):
    if root is None:
        fp.write(str(MARKER) + " ")
        return

    fp.write(str(root.data) + " ")
    serialize(root.left, fp)
    serialize(root.right, fp)


def deSerialize(numList):
    if len(numList) is 0:
        return None

    element = numList.pop(0)

    if element is MARKER:
        return None

    root = Node(element)
    root.left = deSerialize(numList)
    root.right = deSerialize(numList)
    return root


if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    result = []
    inorder(root, result)
    print(result)

    fp = open("tree.txt", "w")
    if fp is None:
        print("Could not open file")
        exit(0)
    serialize(root, fp)
    fp.close()

    fp = open("tree.txt", "r")
    if fp is None:
        print("Could not open file")
        exit(0)
    content = fp.read()
    content = content.rstrip(' ')
    numList = [int(x) for x in content.split(' ')]
    root = deSerialize(numList)
    fp.close()

    result = []
    inorder(root, result)
    print(result)
