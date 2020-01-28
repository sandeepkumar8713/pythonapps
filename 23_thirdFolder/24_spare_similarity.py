# CTCI : Q17_26_Sparse_Similarity
# Question : Sparse Similarity: The similarity of two documents (each with distinct words) is defined to be the
# size of the intersection divided by the size of the union. For example, if the documents consist of
# integers, the similarity of {1, 5, 3} and { 1, 7, 2, 3} is 0. 4, because the intersection has size
# 2 and the union has size 5. We have a long list of documents (with distinct values and each with an
# associated ID) where the similarity is believed to be "sparse:'That is, any two arbitrarily selected
# documents are very likely to have similarity O. Design an algorithm that returns a list of pairs of
# document IDs and the associated similarity. Print only the pairs with similarity greater than 0.
# Empty documents should not be printed at all. For simplicity, you may assume each document is represented
# as an array of distinct integers.
#
# Question Type : Easy
# Used : Compare each document with other document and calculate similarity.
#        Their are nC2 pairs for which similarity is to be calculated.
# Complexity : O(n^2 * m^2) n is count of documents m is size of document

import functools

class Pair:
    def __init__(self, leftId, rightId):
        self.leftId = leftId
        self.rightId = rightId
        self.similarity = 0

    def calculateIntersection(self, doc1, doc2):
        intersection = 0
        for word in doc1:
            if word in doc2:
                intersection += 1
        union = len(doc2) + len(doc1) - intersection
        self.similarity = float(intersection) / float(union)

    def printSimilarity(self):
        print (self.leftId, self.rightId, self.similarity)


def compare(list1,list2):
    if list1[0] == list2[0]:
        return 0
    if list1[0] < list2[0]:
        return -1
    else:
        return 1


def computeIntersections(elements):
    pairs = []
    for i in range(0, len(elements)-1):
        left = elements[i]
        for j in range(i+1, len(elements)):
            right = elements[j]
            pair = Pair(i, j)
            pair.calculateIntersection(left, right)
            pairs.append(pair)
    return pairs


def computeSimilarities(documents):
    elements = []
    for element in documents:
        element.sort()
        elements.append(element)
    elements = sorted(elements, key=functools.cmp_to_key(compare))
    for element in elements:
        print (element)
    return computeIntersections(elements)


if __name__ == "__main__":
    documents = [[1, 3, 4, 9],
            [2, 4, 6, 7, 8],
            [1, 3, 5, 7, 10],
            [2, 4, 5, 6],
            [2, 5, 6, 10],
            [5, 6, 8, 9, 10],
            [4, 5, 6, 8, 10],
            [1, 7, 8],
            [3, 4, 9, 10],
            [0, 1, 5, 10]]
    similarities = computeSimilarities(documents)
    for pairs in similarities:
        pairs.printSimilarity()
