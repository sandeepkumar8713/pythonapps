# https://leetcode.com/problems/sentence-screen-fitting/
# https://medium.com/@rebeccahezhang/leetcode-418-sentence-screen-fitting-9d6258ce116e
# Similar : 24_fourthFolder/20_text_justification
# Question : Given a rows x cols screen and a sentence represented by a list of non-empty words,
# find how many times the given sentence can be fitted on the screen.
# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won’t exceed 100.
# Length of each word is greater than 0 and won’t exceed 10.
# 1 ≤ rows, cols ≤ 20,000.
#
# Example : Input: rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
# Output:1
# Explanation:
# I-had
# apple
# pie-I
# had--
#
# Question Type : Generic
# Used : Concatenate given list into one long string with space after each string.
#        Let n length of long string.
#        Now loop over the given row. Keep track of pos i.e last col of the row.
#        If char at pos is space, we have successfully fit in the row. inc pos
#        Else keep dec pos until we find a space in that row.
#        After loop, return pos / n.
#        Logic :
#        pos = 0, n = len(wholeStmt)
#        for i in range(rows):
#           pos += cols
#           if wholeStmt[pos % n] == " ":
#               pos += 1
#           else:
#               while pos > 0 and wholeStmt[(pos - 1) % n] != " ":
#                   pos -= 1
#        return pos // n
# Complexity : O(m*n) where m and n are rows and count


def wordsTyping(sentence, rows, cols):
    wholeStmt = ""
    for word in sentence:
        wholeStmt += word + " "

    pos = 0
    n = len(wholeStmt)
    for i in range(rows):
        pos += cols
        if wholeStmt[pos % n] == " ":
            pos += 1
        else:
            while pos > 0 and wholeStmt[(pos - 1) % n] != " ":
                pos -= 1

    return pos // n


if __name__ == "__main__":
    rows = 4
    cols = 5
    sentence = ["I", "had", "apple", "pie"]
    print(wordsTyping(sentence, rows, cols))
