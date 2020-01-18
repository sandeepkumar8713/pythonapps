# Question : Print words of a string in reverse order.
# Let there be a string say "I AM A GEEK". So, the output should be "GEEK A AM I" .
#
# Used : split the string with delimiter, traverse it in reverse and append to new string
# Complexity : O(n)


def reverseWords(inputString):
    DELIMITER = ' '
    inputList = inputString.split(DELIMITER)
    newString = ''
    for i in range(len(inputList)-1, -1, -1):
        newString += inputList[i] + ' '
    newString = newString.rstrip(DELIMITER)
    return newString


if __name__ == "__main__":
    inputString = "I AM A GEEK"
    print(reverseWords(inputString))
