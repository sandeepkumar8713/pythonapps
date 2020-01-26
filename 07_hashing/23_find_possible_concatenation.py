# https://www.geeksforgeeks.org/find-starting-indices-substrings-string-s-made-concatenating-words-listl/
# Question : You are given a string S, and a list of words L i.e array/vector of strings (Words in list L are all
# of the same length). Find the starting indices of the substrings in string S, which contains all the words
# present in list L.
#
# Question Type : ShouldSee
# Used : 1. Declare a map (hash_map) which stores all words of List L corresponding to their occurrences inside list L.
#        2. Traverse through all possible substrings in string S which are equal to size_L(total number of characters
#           produced if all the words in list L are concatenated).
#        3. Create a temporary map (temp_hash_map) and initialize it with original map(hash_map) for every possible
#           substring.
#        4. Extract the words from the substring and if the word is present in temp_hash_map we decrease it's
#           corresponding count, if it's not present in temp_hash_map we simply break.
#        5. After traversing the substring we traverse temp_hash_map and look for any key which has it's count > 0.
#           If we found no such key it means that all the words in list L were found in substring and store the
#           given starting index of the substring, if we find a key which has it's count > 0 it means we did not
#           traversed whole substring because we came across a word which was not in temp_hash_map.
# Complexity : O(N - K) * K
#              N : length of string S.
#              K : total length of list L if all the words are concatenated.


def findSubStringIndices(inpStr, words):
    wordSize = len(words[0])
    wordCount = len(words)
    size_L = wordSize * wordCount
    res = []

    if size_L > len(inpStr):
        return res

    # Map stores the words present in list words against it's occurrences inside list L
    hashMap = dict()
    for i in range(wordCount):
        if words[i] in hashMap:
            hashMap[words[i]] += 1
        else:
            hashMap[words[i]] = 1

    for i in range(0, len(inpStr) - size_L + 1, 1):
        temp_hash_map = hashMap.copy()
        j = i
        count = wordCount

        # Traverse the substring
        while j < i + size_L:
            # Extract the word
            word = inpStr[j:j + wordSize]
            # If word not found or if frequency of current word is more than required simply break.
            if word not in hashMap or temp_hash_map[word] == 0:
                break
            # Else decrement the count of word from hash_map
            else:
                temp_hash_map[word] -= 1
                count -= 1
            j += wordSize

        # Store the starting index of that substring when all the words in the list are in substring
        if count == 0:
            res.append(i)
    return res


if __name__ == "__main__":
    inpStr = "barfoothefoobarman"
    words = ["foo", "bar"]
    indices = findSubStringIndices(inpStr, words)
    print(indices)
