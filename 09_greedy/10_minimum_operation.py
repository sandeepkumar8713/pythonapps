# Question : Convert a number m to n with minimum operations. The operations allowed are :
# 1. Divide by 2, i.e., do m = m / 2
# 2. Subtract 1, i.e., do m = m - 1
#
# Question Type : Easy
# Used : call a recursive function which convert(start, end) returns min operation count.
#        If end < 0 return -1
#        If end > start return -1
#        If start == end return 0
#        If (start % 2 is 0) and (start / 2 >= end) : return 1 + convert(start / 2, end)
#           else return 1 + convert(start - 1, end)
#        Here we are tracing the two possible solution from start to end
# Complexity : O(n)


def convert(start, end):
    if end < 0:
        return -1

    if end > start:
        return -1

    if start == end:
        return 0

    if start % 2 is 0 and start / 2 >= end:
        return 1 + convert(start / 2, end)
    else:
        return 1 + convert(start - 1, end)


if __name__ == "__main__":
    start = 11
    end = 3
    # start = 10
    # end = 6

    print("Minimum Operations required :", convert(start, end))
