# https://leetcode.com/problems/h-index/
# Question : Given an array of integers citations where citations[i] is the number of citations a
# researcher received for their ith paper, return compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: A scientist has an index h if h of their
# n papers have at least h citations each, and the other n − h papers have no more than h citations each.
# If there are several possible values for h, the maximum one is taken as the h-index.
#
# Example : Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received
# 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations
# each and the remaining two with no more than 3 citations each, their h-index is 3.
#
# Question Type : ShouldSee
# Used : Sort the given input array in descending order.
#        Loop over the input array, if index + 1 > cit[i] return i
#        Logic : citations.sort(reverse=True)
#        for i in range(N):
#           if i + 1 > citations[i]:
#               return i
#        return N
# Complexity : O(n log n)
#
# TODO ::


def hIndex(citations):
    citations.sort(reverse=True)
    N = len(citations)
    for i in range(N):
        if i + 1 > citations[i]:
            return i
    return N


if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print (hIndex(citations))
