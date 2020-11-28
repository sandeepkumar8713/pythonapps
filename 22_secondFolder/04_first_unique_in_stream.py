# Question : You are given a stream of values, you have to find first unique value at any particular point of time.
#
# Question Type : ShouldSee
# Used : Loop through the stream, keep appending elements in the list if element is not their,
#        if it is their then remove the element from the list. Print the first element of list after
#        each iteration.
# Complexity : O(n)


def findFirstNonRepeating(stream):
    inDLL = []
    for i in range(len(stream)):
        x = stream[i]
        # print "Reading " + x + " from stream"

        if x in inDLL:
            inDLL.remove(x)
        else:
            inDLL.append(x)

        if len(inDLL) != 0:
            print("First non-repeating character so far is ", str(inDLL[0]))


if __name__ == "__main__":
    stream = "geeksforgeeksandgeeksquizfor"
    findFirstNonRepeating(stream)
