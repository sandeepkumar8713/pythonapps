# https://leetcode.com/problems/similar-string-groups/
# Question : Two strings X and Y are similar if we can swap two letters (in different positions)
# of X, so that it equals Y. Also two strings X and Y are similar if they are equal. For example,
# "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar,
# but "star" is not similar to "tars", "rats", or "arts". Together, these form two connected groups
# by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the
# same group even though they are not similar.  Formally, each group is such that a word is in
# the group if and only if it is similar to at least one other word in the group. We are given
# a list strs of strings where every string in strs is an anagram of every other string in strs.
# How many groups are there?
#
# Example : Input: strs = ["tars","rats","arts","star"]
# Output: 2
#
# Question Type : ShouldSee
# Used : We can convert this problem to graph, where each str represents a node.
#        Similarity means diff count b/w 2 str must be less than or equal to 2.
#        The similarity means a edge b/w 2 nodes.
#        Now do parent and union on graph.
#        Return len of disjoint set.
#        Logic :
#        def is_sim(s1, s2):
#        n = len(s1), diff = 0
#        for i in range(n):
#           if s1[i] != s2[i]: diff += 1
#           if diff > 2: break
#        return diff <= 2
#
#        def numSimilarGroups(strs)
#           for i in range(n - 1):
#               for j in range(i + 1, n):
#                   if is_sim(strs[i], strs[j]):
#                       union(i, j, parentArr)
#        ans = set()
#        for i in range(n):
#           ans.add(find(i, parentArr))
#        return len(ans)
# Complexity : O(n^2)


def is_sim(s1, s2):
    n = len(s1)
    diff = 0
    for i in range(n):
        if s1[i] != s2[i]:
            diff += 1
        if diff > 2:
            break
    return diff <= 2


def find(x, parentArr):
    while parentArr[x] != x:
        x = parentArr[x]
    return x


def union(x, y, parentArr):
    parentArr[find(y, parentArr)] = find(x, parentArr)


def numSimilarGroups(strs):
    n = len(strs)

    parentArr = {i: i for i in range(n)}

    for i in range(n-1):
        for j in range(i + 1, n):
            if is_sim(strs[i], strs[j]):
                union(i, j, parentArr)

    ans = set()
    for i in range(n):
        ans.add(find(i, parentArr))

    return len(ans)


if __name__ == "__main__":
    strs = ["tars", "rats", "arts", "star"]
    print(numSimilarGroups(strs))
