# https://www.geeksforgeeks.org/lexicographically-smallest-and-largest-substring-of-size-k/
# Question : Given String str and an integer k, find the lexicographically smallest and largest
# substring of length k
# Lexicography order, also called as alphabetical order or dictionary order
# A < B <... < Y < Z < a < b <.. < y < z
#
# Used : Make a running window of size k and make corresponding sub string.
#           Compare it with min sub string and update if required.
#     currStr = inpStr[:k]
#     for i in range(k, len(inpStr)):
#         currStr = currStr[1: k] + inpStr[i]
#         if lexMax < currStr: lexMax = currStr
#         if lexMin > currStr: lexMin = currStr
#     return lexMin, lexMax
# Complexity : O(n)


def getSmallestAndLargest(inpStr, k):
    currStr = inpStr[:k]
    lexMin = currStr
    lexMax = currStr

    for i in range(k, len(inpStr)):
        currStr = currStr[1: k] + inpStr[i]
        if lexMax < currStr:
            lexMax = currStr

        if lexMin > currStr:
            lexMin = currStr

    print(lexMin)
    print(lexMax)


if __name__ == '__main__':
    str1 = "GeeksForGeeks"
    k = 3
    getSmallestAndLargest(str1, k)
