# https://leetcode.com/problems/number-of-matching-subsequences/
# Question : Given string S and a dictionary of words words, find the number of
# words[i] that is a subsequence of S.
#
# Example : Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
#
# Question Type : ShouldSee
# Used :  Try to use hashing here. Key : char, value : list of indices
#         Loop over the input array. compare each char, see if present, fetch its index, next ele
#           should be present at index the previous index.
#         Logic : def numMatchingSubseq(bigWord, words):
#         res = 0, N = len(words)
#         pointers = [0] * N
#         endset = dict()
#         for i, word in enumerate(words):
#             if word[0] not in endset:
#                 endset[word[0]] = [i]
#             else:
#                 endset[word[0]].append(i)
#         for char in bigWord:
#             newarr = []
#             for i in endset[char]:
#                 pointers[i] += 1
#                 if pointers[i] == len(words[i]):
#                     res += 1
#                 else:
#                     endc = words[i][pointers[i]]
#                     if endc == char:
#                         newarr.append(i)
#                     else:
#                         if endc not in endset.keys():
#                             endset[endc] = [i]
#                         else:
#                             endset[endc].append(i)
#             endset[char] = newarr
#         return res
# Complexity :


def numMatchingSubseq(bigWord, words):
        res = 0
        N = len(words)
        pointers = [0] * N

        endset = dict()

        for i, word in enumerate(words):
            if word[0] not in endset:
                endset[word[0]] = [i]
            else:
                endset[word[0]].append(i)

        for char in bigWord:
            newarr = []
            for i in endset[char]:
                pointers[i] += 1
                if pointers[i] == len(words[i]):
                    res += 1
                else:
                    endc = words[i][pointers[i]]
                    if endc == char:
                        newarr.append(i)
                    else:
                        if endc not in endset.keys():
                            endset[endc] = [i]
                        else:
                            endset[endc].append(i)
            endset[char] = newarr
        return res


if __name__ == "__main__":
    bigWord = "abcde"
    words = ["a", "bb", "acd", "ace"]
    print(numMatchingSubseq(bigWord, words))
