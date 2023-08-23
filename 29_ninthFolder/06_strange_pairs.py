# Question : Given a list of points (x1, y1), (x2, y2), ... (xn, yn), return the biggest subset
# (a1, b1), (a2, b2), ... (am, bm) that meets the following condition:
# 1. a1 < a2 < ... < am
# 2. b1 > b2 > ... > bm
#
# Example: Input : [(5, 6), (2, 8), (4, 1), (1, 9), (3, 7)]
# Output :  [(1, 9), (2, 8), (3, 7), (5, 6)]
#
# Question Type : Generic
# Used : Sort based on first element then do Box stacking.
#        We will get max_len and marker array after box stacking. Use it make the result array.
# Logic: for i in range(1, n):
#           for j in range(i):
#               if pairs[j][0] < pairs[i][0] and pairs[j][1] > pairs[i][1]:
#                   if MSH[j] + 1 > MSH[i]:
#                       MSH[i] = MSH[j] + 1, marker[i] = j
#        max_len = max(MSH)
#        marker_index = MSH.index(max_len)
#        res = []
#        while max_len != 0:
#           res.append(pairs[marker_index])
#           marker_index = marker[marker_index]
#           max_len -= 1
#        res.reverse()
#        return res
# Complexity : O(n^2)

def get_strange_pair(pairs):
    pairs.sort(key=lambda x: x[0])
    n = len(pairs)
    MSH = [1] * n
    marker = [i for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if pairs[j][0] < pairs[i][0] and pairs[j][1] > pairs[i][1]:
                if MSH[j] + 1 > MSH[i]:
                    MSH[i] = MSH[j] + 1
                    marker[i] = j

    max_len = max(MSH)
    marker_index = MSH.index(max_len)
    res = []
    while max_len != 0:
        res.append(pairs[marker_index])
        marker_index = marker[marker_index]
        max_len -= 1

    res.reverse()
    return res


if __name__ == "__main__":
    pairs = [(5, 6), (2, 8), (4, 1), (1, 9), (3, 7)]
    print(get_strange_pair(pairs))

    pairs = [(5, 6), (5, 6), (2, 8), (4, 1), (1, 9), (3, 7)]
    print(get_strange_pair(pairs))
