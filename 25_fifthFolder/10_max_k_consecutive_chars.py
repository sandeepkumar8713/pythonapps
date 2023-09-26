# https://www.geeksforgeeks.org/lexicographically-largest-string-possible-consisting-of-at-most-k-consecutive-similar-characters/
# Question : Given a string S and an integer K, the task is to generate lexicographically the largest string
# possible from the given string, by removing characters also, that consists of at most K consecutive similar
# characters.
#
# Examples:
# Input: S = “baccc”, K = 2
# Output: ccbca
#
# Input: S = “ccbbb”, K = 2
# Output: ccbb
#
# Question Type : Easy, SimilarAdded
# Used : Make a map of character and its frequency for the given input string.
#        Now loop over the map but from 25 to 0 index/ascii. While doing so keep appending the
#        characters in the ansStr. If freq is more than 1, add consecutive characters while
#        decreasing the freq in map. If the given limit is reached, find the next character
#        from the map and append in ansStr. If not found, return the ansStr.
#        After appending the next char, let the loop continue as normal.
#        After loop return the ansStr.
# Logic: for i in range(MAX_CHAR-1, -1, -1):
#           count = 0
#           while charset[i] > 0:
#               newStrings += indexToChar(i)
#               charset[i] -= 1
#               count += 1
#               if charset[i] > 0 and count == limit:
#                   next = nextAvailableChar(charset, i)
#                   if next == '\0':
#                       return newStrings
#                   newStrings += next
#                   count = 0
#        return newStrings
# Complexity : O(n)

MAX_CHAR = 26


def charToIndex(ch):
    return ord(ch) - ord('a')


def indexToChar(index):
    return chr(index + ord('a'))


def nextAvailableChar(charset, start):
    for i in range(start - 1, -1, -1):
        if charset[i] > 0:
            charset[i] -= 1
            return indexToChar(i)

    return '\0'


def newString(originalLabel, limit):
    n = len(originalLabel)
    charset = [0] * MAX_CHAR
    newStrings = ""

    for ch in originalLabel:
        charset[charToIndex(ch)] += 1

    for i in range(MAX_CHAR-1, -1, -1):
        count = 0
        while charset[i] > 0:
            newStrings += indexToChar(i)
            charset[i] -= 1
            count += 1
            if charset[i] > 0 and count == limit:
                next = nextAvailableChar(charset, i)
                if next == '\0':
                    return newStrings
                newStrings += next
                count = 0
    return newStrings


if __name__ == "__main__":
    S = "ccbbb"
    K = 2
    print(newString(S, K))

    S = "baccc"
    K = 2
    print(newString(S, K))
