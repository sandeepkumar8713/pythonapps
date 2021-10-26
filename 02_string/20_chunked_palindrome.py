# https://www.geeksforgeeks.org/longest-possible-chunked-palindrome/
# Question : Given a string, the task is to return the length of its longest possible
# chuncked palindrome. It means a palindrome formed by substring in the case when it is
# not formed by characters of the string. For better understanding look at the example.
#
# Input : ghiabcdefhelloadamhelloabcdefghi
# Output : 7
# (ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)
#
# Question Type : ShouldSee
# Used : The idea is to have two pointer on left and right of the given string. Check
#        if left and right substring are of same length.. If yes, call recursive
#        function over remaining substring.
#        LPCUtil(currStr, chunkCount, processedLength, originalLen):
#        if len(currStr) == 0: return chunkCount
#        if len(currStr) == 1:
#           if chunkCount != 0 and (originalLen - processedLength) <= 1:
#               return chunkCount + 1
#           else:
#               return 1
#        n = len(currStr)
#        for i in range(0, n // 2):
#           leftChunk = currStr[0:i+1]
#           rightChunk = currStr[n-1-i:n]
#           if leftChunk == rightChunk:
#               return LPCUtil(currStr[i+1:n-1-i], chunkCount + 2, processedLength + (i+1)*2, originalLen)
#        return chunkCount + 1
# Complexity : O(n log n)


def LPCUtil(currStr, chunkCount, processedLength, originalLen):
    if len(currStr) == 0:
        return chunkCount

    if len(currStr) == 1:
        if chunkCount != 0 and (originalLen - processedLength) <= 1:
            print('(' + currStr + ')')
            return chunkCount + 1
        else:
            return 1

    n = len(currStr)
    for i in range(0, n // 2):
        leftChunk = currStr[0:i+1]
        rightChunk = currStr[n-1-i:n]
        if leftChunk == rightChunk:
            print ('(' + leftChunk + ')' + ' (' + rightChunk + ')')
            return LPCUtil(currStr[i+1:n-1-i], chunkCount + 2, processedLength + (i+1)*2, originalLen)

    print ('(' + currStr + ')')
    return chunkCount + 1


def LPC(inpStr):
    return LPCUtil(inpStr, 0, 0, len(inpStr))


if __name__ == "__main__":
    # word = "VOLVO"
    # word = "VOLLOV"
    # word = "geeksforgeeks"
    # word = "merchant"
    word = "ghiabcdefhelloadamhelloabcdefghi"
    # word = "antaprezatepzapreanta"
    print(LPC(word))
