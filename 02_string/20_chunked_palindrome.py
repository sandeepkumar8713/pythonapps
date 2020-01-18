# https://www.geeksforgeeks.org/longest-possible-chunked-palindrome/
# Question : Given a string, the task is to return the length of its longest possible chuncked palindrome. It means
# a palindrome formed by substring in the case when it is not formed by characters of the string. For better
# understanding look at the example.
#
# Input : ghiabcdefhelloadamhelloabcdefghi
# Output : 7
# (ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)
#
# Used : The idea is to have two pointer on left and right of the given string. Check if left and right substring of
#           same length is equal. If yes, call recursive function over remaining substring.
#        We call a recursive function LPCUtil(currStr, chunkCount, processedLength, originalLen) with initial input :
#           LPCUtil(inpStr, 0, 0, len(inpStr))
#        If len(currStr) == 0: return chunkCount
#        If len(currStr) == 1: If chunkCount != 0 and (originalLen - processedLength) is less than or equal to 1: return 0
#           Else return 1
#        Now loop over currStr for i : 0 to n/2. Compute left and right substring of length i+1.
#        leftChunk = currStr[0:i+1] and rightChunk = currStr[n-1-i:n]
#        If above are same, call func on remaining substring after increasing chunkCount and processedLength.
#           return LPCUtil(currStr[i+1:n-1-i], chunkCount + 2, processedLength + (i+1)*2, originalLen)
#        If we come out of loop that means that given currStr can't be chucked further so return chunkCount + 1
# Complexity : O(n log n)


def LPCUtil(currStr, chunkCount, processedLength, originalLen):
    if len(currStr) == 0:
        return chunkCount

    if len(currStr) == 1:
        if chunkCount != 0 and (originalLen - processedLength) <= 1:
            print '(' + currStr + ')'
            return chunkCount + 1
        else:
            return 1

    n = len(currStr)
    for i in range(0, n/2):
        leftChunk = currStr[0:i+1]
        rightChunk = currStr[n-1-i:n]
        if leftChunk == rightChunk:
            print '(' + leftChunk + ')' + ' (' + rightChunk + ')'
            return LPCUtil(currStr[i+1:n-1-i], chunkCount + 2, processedLength + (i+1)*2, originalLen)

    print '(' + currStr + ')'
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
    print (LPC(word))
