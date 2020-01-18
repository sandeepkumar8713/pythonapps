# https://leetcode.com/discuss/interview-question/391709/
# Question : Given a number z C N and a function f(x, y) C N, where x C N and y C N.
# Function f(x, y) is black box and unknown but we can pass any x and y to function and get f(x, y) value.
# f(x, y) is strictly increasing:
# f(x, y) < f(x + 1, y)
# f(x, y) < f(x, y + 1)
# Find all pairs of x and y, where f(x, y) = z.
#
# Used : Because f is strictly monotonously increasing, we can use binary search to find a suiting y for a given x.
#        Once I find a y for x=1, I try increasingly larger x=2,3,... using the previously found y as an upper
#        bound for the binary search.
#        We do binary search on pair while y >= 1 and f(x,1) <= z. i.e. keep decreasing y and increasing x.
#        Make function, which take either 1 argument as constant and other one as variable, so that we can interchange
#        arguments when required.
#        Logic : def binSearch(f, z, const, isXConst):  # find smallest t such that g(t) >= z
#        low, high = 0, 1
#        while withConstant(f, const, isXConst, high) < z: high *= 2
#        while low < high:
#           mid = (low + high) // 2
#           if withConstant(f, const, isXConst, mid) < z: low = mid + 1
#           else: high = mid
#        return low + 1
#        def findFunctionArguments(f, z):
#        ans = [], x = 1
#        y = binSearch(f, z, x, True)
#        while y >= 1 and f(x, 1) <= z:
#           if f(x, y) > z: y = binSearch(f, z, x, True)
#           elif f(x, y) < z: x = binSearch(f, z, y, False) - 1
#           if f(x, y) > z: y -= 1
#           elif f(x, y) < z: x += 1
#           else: ans.append([x, y]), y -= 1
#        return ans
# Complexity : O(log n * log n)


def withConstant(f, const, isXConst, argument):
    if isXConst:
        return f(const, argument)
    else:
        return f(argument, const)


def binSearch(f, z, const, isXConst):
    # find smallest t such that g(t) >= z
    low, high = 0, 1
    while withConstant(f, const, isXConst, high) < z:
        high *= 2

    while low < high:
        mid = (low + high) // 2
        if withConstant(f, const, isXConst, mid) < z:
            low = mid + 1
        else:
            high = mid
    return low + 1


def findFunctionArguments(f, z):
    ans = []
    x = 1
    y = binSearch(f, z, x, True)

    while y >= 1 and f(x, 1) <= z:
        # use binary search to speed up
        if f(x, y) > z:
            y = binSearch(f, z, x, True)
        elif f(x, y) < z:
            x = binSearch(f, z, y, False) - 1
        # check (x, y) again
        if f(x, y) > z:
            y -= 1
        elif f(x, y) < z:
            x += 1
        else:
            ans.append([x, y])
            y -= 1

    return ans


if __name__ == "__main__":
    f = lambda x, y: x + y
    z = 5
    print(findFunctionArguments(f, z))

    f = lambda x, y: x * x + y
    z = 50
    print(findFunctionArguments(f, z))

    f = lambda x, y: x + (y - 1) * 0xFFFFFFFE
    z = 0xFFFFFFFF
    print(findFunctionArguments(f, z))
