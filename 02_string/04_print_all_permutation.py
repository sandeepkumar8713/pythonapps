# Question : Write a program to print all permutations of a given string.
# For input ABC.
#
# Question Type : Easy
# Used : backtrack
#        Fix a element on left, keep replacing every element on the right side and print
#        and then backtrack.
#        Call a recursive function permute(a, l, r) with input permute(a, 0, n - 1).
#        If l == r : print a
#        else: loop for i : l to r:
#           swap a[l] and a[i]
#           call recursive function again permute(a, left + 1, right)
#           swap a[l] and a[i]
# Complexity : O(n!)


def toString(List):
    return ''.join(List)


def permute(a, left, right):
    if left == right:
        print(toString(a))
    else:
        for i in range(left, right + 1):
            a[left], a[i] = a[i], a[left]
            permute(a, left + 1, right)
            a[left], a[i] = a[i], a[left]  # backtrack


if __name__ == "__main__":
    string = "ABC"
    n = len(string)
    a = list(string)
    permute(a, 0, n - 1)
