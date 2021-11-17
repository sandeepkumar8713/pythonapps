# https://leetcode.com/problems/push-dominoes/
# Question : There are n dominoes in a line, and we place each domino vertically upright. In
# the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left.
# Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
# When a vertical domino has dominoes falling on it from both sides, it stays still due to
# the balance of the forces.For the purposes of this question, we will consider that a falling
# domino expends no additional force to a falling or already fallen domino.
# You are given a string dominoes representing the initial state where:
# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state.
#
# Example : Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
#
# Question Type : Generic
# Used : Convert the given input array into -1, 0 and 1.
#        Loop over the array, If current ele is 0, its final state is sum of left and right elem.
#        After the loop, update the ans with char.
#        Logic :
#        tempArr = [0]
#        for item in dominoes:
#           tempArr.append(map[item])
#        tempArr.append(0)
#        for i in range(1, len(tempArr) - 1):
#           if tempArr[i] == 0:
#               left = tempArr[i - 1]
#               if tempArr[i - 1] == -1: left = 0
#               right = tempArr[i + 1]
#               if tempArr[i + 1] == 1: right = 0
#               ans.append(reverseMap[left + right])
#           else:
#               ans.append(reverseMap[tempArr[i]])
#        return "".join(ans)
# Complexity : O(n)

map = {"L": -1, "R": 1, ".": 0}
reverseMap = {-1: "L", 1: "R", 0: "."}


def getFinalState(dominoes):
    n = len(dominoes)
    tempArr = [0]
    for item in dominoes:
        tempArr.append(map[item])
    tempArr.append(0)

    ans = []
    for i in range(1, len(tempArr) - 1):
        if tempArr[i] == 0:
            left = tempArr[i - 1]
            if tempArr[i - 1] == -1:  # won't exert pressure
                left = 0

            right = tempArr[i + 1]
            if tempArr[i + 1] == 1:  # won't exert pressure
                right = 0

            ans.append(reverseMap[left + right])
        else:
            ans.append(reverseMap[tempArr[i]])

    return "".join(ans)


if __name__ == "__main__":
    dominoes = ".L.R...LR..L.."
    print(getFinalState(dominoes))

    dominoes = "RR.L"
    print(getFinalState(dominoes))
