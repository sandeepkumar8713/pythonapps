# https://leetcode.com/problems/ambiguous-coordinates/
# Question : We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all
# commas, decimal points, and spaces and ended up with the string s.
#
# Example: "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)"
#
# Question Type : Generic
# Used : Run a loop from 2 to n - 1 and place comma at each place.
#        For each left and right substr call generate which places dot at all possible places.
#        Now merge the all possible left and right substr.
#        Note : placing dot we should take take there should not be extra at prefix and suffix of dot.
#        Logic :
#        for i in range(2, n - 1):
#           cand_l, cand_r = generate(inpStr[1:i]), generate(inpStr[i:-1])
#           for l in cand_l:
#               for r in cand_r:
#                   ans.append("(" + l + ", " + r + ")")
#        def generate(inpStr):
#        ans = []
#        if inpStr == "0" or inpStr[0] != "0": ans.append(inpStr)
#        for i in range(1, len(inpStr)):
#           if (inpStr[:i] == "0" or inpStr[0] != "0") and inpStr[-1] != "0":
#               ans.append(inpStr[:i] + "." + inpStr[i:])
#        return ans
# Complexity : O(n^3)


def generate(inpStr):
    ans = []
    if inpStr == "0" or inpStr[0] != "0":
        ans.append(inpStr)

    for i in range(1, len(inpStr)):
        if (inpStr[:i] == "0" or inpStr[0] != "0") and inpStr[-1] != "0":
            ans.append(inpStr[:i] + "." + inpStr[i:])

    return ans


def ambiguousCoordinates(inpStr):
    n, ans = len(inpStr), []

    for i in range(2, n - 1):
        cand_l, cand_r = generate(inpStr[1:i]), generate(inpStr[i:-1])

        for l in cand_l:
            for r in cand_r:
                ans.append("(" + l + ", " + r + ")")

    return ans


if __name__ == "__main__":
    S = "(123)"
    print(ambiguousCoordinates(S))
