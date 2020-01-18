# CTCI : Q1_03_URLify
# Question : Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string.
#
# Input : 'Mr John Smith    '
# Output : Mr%20John%20Smith
#
# Used : Find true length without trailing space. Find space count within true length. Now calculate newIndex
#        (trueLength + (spaceCount * 2). Make a empty list listStr of size newIndex. Now start filling the listStr in
#        reverse. While doing so replace ' ' with %20.
# Complexity : O(n)


def urlify(inpStr):
    trueLength = len(inpStr)
    spaceCount = 0
    for i in range(len(inpStr) - 1, -1, -1):
        if inpStr[i] != ' ':
            break
        else:
            trueLength -= 1

    for i in range(trueLength):
        if inpStr[i] == ' ':
            spaceCount += 1

    newIndex = trueLength + (spaceCount * 2)
    listStr = ['0'] * newIndex
    for i in range(trueLength-1, -1, -1):
        if inpStr[i] == ' ':
            # python list insertion right is not involved
            listStr[newIndex-3:newIndex] = "%20"
            newIndex -= 3
            pass
        else:
            listStr[newIndex - 1] = inpStr[i]
            newIndex -= 1

    str1= ""
    return str1.join(listStr)


if __name__ == "__main__":
    print(urlify('Mr John Smith    '))
    print(urlify('Mr John Smith'))
    print(urlify('Mr John '))
