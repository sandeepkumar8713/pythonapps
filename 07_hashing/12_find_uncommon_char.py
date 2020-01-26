# Question : Find and print the uncommon characters of the two given strings in sorted order. Here uncommon
# character means that either the character is present in one string or it is present in other string but not
# in both. The strings contain only lowercase characters and can contain duplicates.
#
# Used : Loop over the elements of string1 and push in hash dict while marking its value as 1
#        Loop over the elements of string2 and if the element is present in hashDict mark it as -1 else insert in hash
#           dict with value 2
#        Loop over the elements of hashDict and print the keys whose value is 1 or 2
# Complexity : O(n)


def findUncommon(str1, str2):
    hashDict = dict()
    for ele in str1:
        hashDict[ele] = 1

    for ele in str2:
        if ele in hashDict.keys():
            hashDict[ele] = -1
        else:
            hashDict[ele] = 2

    for ele,value in hashDict.items():
        if value == 1 or value == 2:
            print(ele, end=" ")


if __name__ == "__main__":
    str1 = "characters"
    str2 = "alphabets"
    findUncommon(str1, str2)
