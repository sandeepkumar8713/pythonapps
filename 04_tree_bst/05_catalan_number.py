# https://www.geeksforgeeks.org/total-number-of-possible-binary-search-trees-with-n-keys/
# Question : Total number of possible Binary Search Trees with n different keys
# (countBST(n)) = Catalan number Cn = (2n)!/(n+1)!*n!
#
# For n = 0, 1, 2, 3, ... values of Catalan numbers are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862,
# ...So are numbers of Binary Search Trees.
#
# Question Type : ShouldSee
# Used : Let's say node i is chosen to be the root. Then there are i - 1 nodes smaller than i and n - i
#        nodes bigger than i. For each of these two sets of nodes, there is a certain number of possible
#        subtrees. Let t(n) be the total number of BSTs with n nodes. The total number of BSTs with i at
#        the root is t(i - 1) t(n - i). The two terms are multiplied together because the arrangements in
#        the left and right subtrees are independent. That is, for each arrangement in the left tree and for
#        each arrangement in the right tree, you get one BST with i at the root.
#        Summing over i gives the total number of binary search trees with n nodes.
#        t(n) = {n (Summation) i = 1}  t(i-1)*t(n-i)
#
#        The base case is t(0) = 1 and t(1) = 1, i.e. there is one empty BST and there is one BST with one node.
#        t(2) = t(1)t(0) + t(0)t(1)
#        t(3) = t(0)t(2) + t(1)t(1) + t(2)t(0)
# Complexity : O(n)


def binomialCoeff(n, k):
    res = 1
    # Since C(n, k) = C(n, n - k)
    if k > n - k:
        k = n - k

    # Calculate value of [n * (n - 1) * --- * (n - k + 1)] / [k * (k - 1) * --- * 1]
    for i in range(k):
        res *= (n - i)
        res /= (i + 1)

    return res


def catalan(n):
    c = binomialCoeff(2*n, n)
    # return 2nCn/(n+1)
    return c/(n+1)


if __name__ == "__main__":
    print(catalan(5))
