# https://www.geeksforgeeks.org/searching-for-patterns-set-5-finite-automata/
# https://www.geeksforgeeks.org/pattern-searching-set-5-efficient-constructtion-of-finite-automata/
# Question : Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function
# search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[].
# You may assume that n > m.
#
# Input:  txt[] = "THIS IS A TEST TEXT"
#         pat[] = "TEST"
# Output: Pattern found at index 10
#
# Question Type : OddOne
# Used : TODO :: add used
# Complexity : computeTF() is O(m^3*NO_OF_CHARS) where m is length of the pattern and
#              NO_OF_CHARS is 256, search(n)

NO_OF_CHARS = 256


def getNextState(pat, m, state, x):
    # calculate the next state

    # If the character c is same as next character in pattern, then simply increment state
    if state < m and x == ord(pat[state]):
        return state + 1

    i = 0
    # ns finally contains the longest prefix which is also suffix in "pat[0..state-1]c"
    # Start from the largest possible value and stop when you find a prefix which is also suffix
    for nextState in range(state, 0, -1):
        if ord(pat[nextState - 1]) == x:
            while i < nextState - 1:
                if pat[i] != pat[state - nextState + 1 + i]:
                    break
                i += 1
            if i == nextState - 1:
                return nextState
    return 0


def computeTF(pat):
    # This function builds the TF table which represents Finite Automata for a given pattern
    global NO_OF_CHARS

    TF = []
    for row in range(len(pat) + 1):
        TF.append([0] * NO_OF_CHARS)

    for state in range(len(pat) + 1):
        for x in range(NO_OF_CHARS):
            # called for x : 0 to 255
            TF[state][x] = getNextState(pat, len(pat), state, x)

    return TF


def search(pat, txt):
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat)

    # Check if I start from state 0 can I reach state M, with input txt[0] to txt[i].
    state = 0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        # if 0 <= i <= 3 or 9 <= i <= 12 or 13 <= i <= 16:
        #     print state
        if state == M:
            print("Pattern found at index:", str(i - M + 1))


if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    # txt = "AABAABA"
    pat = "AABA"
    search(pat, txt)

    print("")

    txt = "GEEKSGEEKS"
    pat = "GEEKS"
    search(pat, txt)
