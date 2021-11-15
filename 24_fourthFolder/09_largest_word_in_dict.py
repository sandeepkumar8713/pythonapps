# https://www.geeksforgeeks.org/find-largest-word-dictionary-deleting-characters-given-string/
# Question : Giving a dictionary and a string 'str', find the longest string in dictionary which can be formed by
# deleting some characters of the given 'str'.
#
# Example :
# Input  : dict = {"pintu", "geeksfor", "geeksgeeks",
#                                         " forgeek"}
#          str = "geeksforgeeks"
# Output : geeksgeeks
#
# Question Type : Generic
# Used : We traverse all dictionary words and for every word,
#        we check if it is sub sequence of given string and is largest of all such words.
#        We finally return the longest word with given string as sub sequence.
#       def isSubSequence(str1,str2):
#           i=0, j=0
#           while i < n and j < m:
#               if str1[j] == str2[i]:
#                   j += 1
#               i += 1
#           return j == m
# Complexity : O(K * m) k is length of dict and m is length of largest word


def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)

    j = 0
    i = 0
    while i < n and j < m:
        if str1[j] == str2[i]:
            j += 1
        i += 1

    return j == m


def findLongestString(dict1, str1):
    result = ""
    length = 0

    for word in dict1:
        if length < len(word) and isSubSequence(word, str1):
            result = word
            length = len(word)

    return result


if __name__ == "__main__":
    dict1 = ["ale", "apple", "monkey", "plea"]
    str1 = "abpcplea"
    print(findLongestString(dict1, str1))
