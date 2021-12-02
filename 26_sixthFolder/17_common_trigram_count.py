# Question : Given 2 lists of words find count of common trigram.
# Follow up question, Given m lists of words and another list of words k. Find count of
# common trigram in each of m lists. Output : {doc1 : 6, doc2 : 7, doc3 : 9}
# trigram : A sequence of 3 consecutive words in document.
#
# Question Type : Asked
# Used : For question 1, make 2 hashsets of given lists with element as concatenation of 3
#        words consecutive and do intersection of the set. Its len is ans.
#        For question 2, We will do preprocessing. Make a map where key : 3 concatenated words
#        value : list of doc ids. Now loop over words in k, for each trigram check if it
#        is present in map and update freq map. Return freq map.
# Complexity : question 1 O(n) where n is len of words list
#              question 2 O(n*m) where m is count of lists
#
# TODO :: add code
#