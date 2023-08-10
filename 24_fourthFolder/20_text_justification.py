# https://massivealgorithms.blogspot.com/2014/06/leetcode-text-justification-darrens-blog.html
# https://leetcode.com/problems/text-justification/
# Question : Given an array of words and a length L, format the text such that each line has exactly L
# characters and is fully (left and right) justified. You should pack your words in a greedy approach;
# that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly L characters. Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words, the empty slots on the left will
# be assigned more spaces than the slots on the right. For the last line of text, it should be left
# justified and no extra space is inserted between words.
# A line other than the last line might contain only one word. What should you do in this case?
# In this case, that line should be left-justified.
#
# Example:
# Input : words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
# Output :
# [  "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
#
# Question Type : ShouldSee
# Used : First calculate how many words with 1 space can be added in a row.
#        Now calculate average and remainder space, to filled in that row.
#        avg = (constLen - rowLen) / wordCount
#        remainder = (constLen - rowLen) % wordCount
#        For last row set avg = rem = 0
#        Now after each word, add avg space and 1 remainder space. That is how we will get justified line
# Logic: while i < n:
#           j = i
#           rowLen = len(words[i])
#           while i < n-1 and rowLen + len(words[i+1]) + 1 <= constLen:
#               rowLen += 1 + len(words[i+1])
#               i += 1
#           avg = (constLen - rowLen) / (j-i)
#           remainder = (constLen - rowLen) % (j-i)
#           thisRow = list(words[j])
#           while j < i:
#               thisRow.extend(spaces[0:avg+1])
#               if rem > 0:
#                   thisRow.append(' ')
#                   rem -= 1
#                j += 1
#               thisRow.extend(list(words[j]))
#           thisRow.extend(spaces[0:constLen - len(thisRow)])
#           resList.append(string.join(thisRow))
#           i += 1
# Complexity : O(n)


def fullJustify(words, constLen):
    resList = []
    n = len(words)
    spaces = [' '] * constLen
    i = 0
    while i < n:
        j = i
        rowLen = len(words[i])
        while i < n-1 and rowLen + len(words[i+1]) + 1 <= constLen:
            rowLen += 1 + len(words[i+1])
            i += 1

        left = j == i or i == n-1
        if left:
            avg = 0
        else:
            avg = (constLen - rowLen) // (i - j)   # spaceCount / wordCount
        if left:
            rem = 0
        else:
            rem = (constLen - rowLen) % (i - j)  # spaceCount % wordCount
        thisRow = list(words[j])
        while j < i:
            thisRow.extend(spaces[0:avg+1])
            if rem > 0:
                thisRow.append(' ')
                rem -= 1
            j += 1
            thisRow.extend(list(words[j]))
        thisRow.extend(spaces[0:constLen - len(thisRow)])
        string = ""
        resList.append(string.join(thisRow))
        i += 1

    return resList


if __name__ == "__main__":
    # words = ["This", "is", "an", "example", "of", "text", "justification."]
    # constLen = 16

    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to",
             "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    constLen = 20

    resList = fullJustify(words, constLen)
    for item in resList:
        print(item)
