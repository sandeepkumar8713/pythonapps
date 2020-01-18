# Question : Given a stream of characters, find the first non-repeating character from stream. You need to tell the first
# non-repeating character in O(1) time at any moment.
#
# Used : The DLL contains all non-repeating characters in order, i.e., the head of DLL contains first non-repeating
# character, the second node contains the second non-repeating and so on. We also maintain two arrays: one array is to
# maintain characters that are already visited two or more times, we call it repeated[], the other array is array of
# pointers to linked list nodes, we call it inDLL[].
# Complexity : O(1) Note that appending a new node to DLL is O(1) operation if we maintain tail pointer. Removing a
# node from DLL is also O(1). So both operations, addition of new character and finding first non-repeating character
# take O(1) time.

MAX_CHAR = 256


def findFirstNonRepeating(stream):
    inDLL = [] * MAX_CHAR
    repeated = [False] * MAX_CHAR

    for i in xrange(len(stream)):
        x = stream[i]
        print "Reading " + x + " from stream"

        if not repeated[ord(x)]:

            # If the character is not in DLL, then add this
            # at the end of DLL
            if not x in inDLL:
                inDLL.append(x)
            else:
                inDLL.remove(x)
                repeated[ord(x)] = True

        if len(inDLL) != 0:
            print "First non-repeating character so far is ",
            print str(inDLL[0])
        else:
            print "no non-repeating character",
            print str(-1)


if __name__ == "__main__":
    stream = "aabc"
    #stream = "geeksforgeeksandgeeksquizfor"
    findFirstNonRepeating(stream)
