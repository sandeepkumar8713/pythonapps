# https://www.geeksforgeeks.org/the-celebrity-problem/
# Question : In a party of N people, only one person is known to everyone. Such a person may be present
# in the party, if yes, (s)he doesn't know anyone in the party. We can only ask questions like "does A know B? ".
# Find the stranger (celebrity) in minimum number of questions.
# If A knows B, then A can't be celebrity. Discard A, and B may be celebrity.
# If A doesn't know B, then B can't be celebrity. Discard B, and A may be celebrity.
#
# Used : Take left and right pointer. Loop while left < right: if mat[left][right] left += 1 else right -= 1.
#        After the loop left might be the celebrity. Loop over from 0 to n-1 and check if left doesn't know anybody
#        and everybody knows left. If true, return left.
# Complexity : O(n)


def findCelebrity(mat):
    n = len(mat)
    left = 0
    right = n - 1

    while left < right:
        if mat[left][right]:
            # knows, So left can be celebrity
            left += 1
        else:
            # does not know, so left may be celebrity
            right -= 1

    # left might be celebrity
    for i in range(n):
        # Send false if left knows someone or if someone doesn't know left
        if left != i and (mat[left][i] == 1 or mat[i][left] == 0):
            return -1
    return left


if __name__ == "__main__":
    mat = [[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 1, 0]]

    print "Index:", findCelebrity(mat)
