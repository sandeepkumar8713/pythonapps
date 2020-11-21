# https://leetcode.com/problems/linked-list-components/
# Question : We are given head, the head node of a linked list containing unique integer values.
# We are also given the list G, a subset of the values in the linked list.
# Return the number of connected components in G, where two values are connected if they appear
# consecutively in the linked list.
#
# Example : Input:
# head: 0->1->2->3
# G = [0, 1, 3]
# Output: 2
# Explanation:
# 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
#
# Question Type : Generic
# Used : Loop over the linked list. If the current element is in G and next element is not in G, then inc the count.
#        Logic : def numComponents(head, G):
#        Gset = set(G)
#        cur = head, ans = 0
#        while cur.next:
#           if (cur.val in Gset and cur.next.val not in Gset):
#               ans += 1
#           cur = cur.next
#        ans += 1
#        return ans
# Complexity : O(n)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def numComponents(head, G):
    Gset = set(G)
    cur = head
    ans = 0
    while cur.next:
        if (cur.data in Gset and cur.next.data not in Gset):
            ans += 1
        cur = cur.next

    ans += 1
    return ans


if __name__ == "__main__":
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    G = [0, 1, 3]

    print(numComponents(head, G))
