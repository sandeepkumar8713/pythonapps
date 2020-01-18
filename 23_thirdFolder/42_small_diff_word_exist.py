# https://www.careercup.com/question?id=5703991611097088
# Question : Find nearest word from the given non-english dictionary which is one off character.
# (could be non ascii characters) for eg. dictionary contains { apple, pineapple, banana, orange }
# if given word "applx" then return true, as applx matches with apple and only one character is off.
# aplpe returns false
#
# Used : An alternative O(n*n) solution would be to preprocess the dictionary into a hash map thus: for every
#        dictionary word w of length q add q words to the hashmap which can be created by removing q-th letter from
#        the word w. Example: for the word 'dog' we add 'og', 'dg', 'do' into the hashmap. Then for the input word we
#        do a similar thing: remove i-th letter and see if the resultant word is in the hashmap
#        Logic : def preprocessDict(words):
#        hmap = set()
#        for word in words:
#           for i in range(len(word)):
#               hmap.add(word[:i] + word[i+1:])
#        return hmap
#        def wordExists(wordDict, word):
#        for i in range(len(word)):
#           if (word[:i] + word[i+1:]) in wordDict:
#               return True
#         return False
# Complexity : O(m) search O(m * n) pre-process


def preprocessDict(words):
    hmap = set()
    for word in words:
        for i in range(len(word)):
            hmap.add(word[:i] + word[i+1:])
    return hmap


def wordExists(wordDict, word):
    for i in range(len(word)):
        if (word[:i] + word[i+1:]) in wordDict:
            return True
    return False


if __name__ == "__main__":
    words = ['apple', 'apple', 'banana', 'orange']
    wordDict = preprocessDict(words)

    print (wordExists(wordDict, 'aPple'))
