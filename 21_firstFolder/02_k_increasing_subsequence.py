# Question : Given an array of integers, find out number of ways in which you can select
# increasing and decreasing sub sequences of length k(k<=n). for eg array is 1 4 6 2 5 & k=3
# then the answer is :- 1 4 5, 1 2 5,1 4 6
#
# Question Type : Generic
# Used : backtracking
# Logic: subSequenceInc(a, n, k, v, idx):
#        if len(v) == k:
#           print(v)
#           return
#        for i in range(idx, n):
#           if len(v) == 0 or a[i] > v[-1]:
#               v.append(a[i])
#               subSequenceInc(a, n, k, v, i+1)
#               v.pop()
# Complexity : O(n^2)


def subSequenceInc(a, n, k, v, idx):
    if len(v) == k:
        print(v)
        return
    for i in range(idx, n):
        if len(v) == 0 or a[i] > v[-1]:
            v.append(a[i])
            subSequenceInc(a, n, k, v, i+1)
            v.pop()


def subSequenceDec(a, n, k, v, idx):
    if len(v) == k:
        print(v)
        return
    for i in range(idx, n):
        if len(v) == 0 or a[i] < v[-1]:
            v.append(a[i])
            subSequenceDec(a, n, k, v, i+1)
            v.pop()


if __name__ == "__main__":
    a = [1, 4, 6, 2, 5, 9, 3]
    # a = [1,4,6,2,5]
    k = 3
    v = []
    print('increasing :')
    subSequenceInc(a, len(a), k, v, 0)
    print('decreasing :')
    v = []
    subSequenceDec(a, len(a), k, v, 0)
