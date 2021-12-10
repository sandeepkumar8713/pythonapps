# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
# Question : With respect to a given puzzle string, a word is valid if both the following
# conditions are satisfied: word contains the first letter of puzzle.
# For each letter in word, that letter is in puzzle.
# For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and
# "baggage", while invalid words are "beefed" (does not include 'a') and "based" (includes
# 's' which is not in the puzzle).
# Return an array answer, where answer[i] is the number of words in the given word list
# words that is valid with respect to the puzzle puzzles[i].
#
# Example : Input: words = ["aaaa","asas","able","ability","actt","actor","access"],
#          puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# Output: [1,1,3,2,4,0]
# Explanation:
# 1 valid word for "aboveyz" : "aaaa"
# 1 valid word for "abrodyz" : "aaaa"
# 3 valid words for "abslute" : "aaaa", "asas", "able"
# 2 valid words for "absoryz" : "aaaa", "asas"
# 4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
# There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
#
#
# Question Type : ShouldSee
# Used : Make bit vector of word in words list and save the same in dict with freq.
#        Now loop over puzzles. For each puzzle, make bit vector of all possible combo and
#        check if same is present in freq map and increment same count.
#        After the loop, return the counter array.
#        Logic:
#        for word in words:
#           bitvector = getBitVector(word)
#           freqMap[bitvector] = freqMap.get(bitvector, 0) + 1
#        res = []
#        for puzzle in puzzles:
#           puzzleBitVector = getBitVector(puzzle)
#           possibleCombo = puzzleBitVector
#           first = (1 << ord(puzzle[0]) - ord('a'))
#           count = 0
#           while possibleCombo:
#               if possibleCombo & first:
#                   count += freqMap.get(possibleCombo, 0)
#             # By using this logic we make all possible combo
#               possibleCombo = (possibleCombo - 1) & puzzleBitVector
#               res.append(count)
#        return res
# Complexity : O(n * 2^7) as puzzle word length is 7.

def getBitVector(word):
    bitVector = 0
    for ch in word:
        bitVector |= (1 << ord(ch) - ord('a'))

    return bitVector


def findNumofValidWords(words, puzzles):
    freqMap = dict()
    for word in words:
        bitvector = getBitVector(word)
        freqMap[bitvector] = freqMap.get(bitvector, 0) + 1

    res = []
    for puzzle in puzzles:
        puzzleBitVector = getBitVector(puzzle)
        possibleCombo = puzzleBitVector
        first = (1 << ord(puzzle[0]) - ord('a'))
        count = 0

        while possibleCombo:
            if possibleCombo & first:
                count += freqMap.get(possibleCombo, 0)

            # unset right most set bit of possibleCombo
            # By using this logic we make all possible combo
            possibleCombo = (possibleCombo - 1) & puzzleBitVector
            # 0b110000000100000010011 puzzleBitVector
            # 0b110000000100000010010 submask1
            # 0b110000000100000010001 submask2

        res.append(count)

    return res


if __name__ == "__main__":
    words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
    puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
    print(findNumofValidWords(words, puzzles))

    words = ["asas"]
    puzzles = ["abslute"]
    print(findNumofValidWords(words, puzzles))
