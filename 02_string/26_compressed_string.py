# CTCI : Q1_06_String_Compression
# Question : implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
#
# Used : Keep a counter countConsecutive = 0. Run a loop over given string. Keep incrementing countConsecutive,
#        If the next char is not equal (or last char), then append the char and its count in the output list.
#        After the loop, if length of output list is less than length of inpStr, then return outputList.
# Complexity : O(n)


def compress(inpStr):
    compressedList = []
    countConsecutive = 0
    for i in range(0, len(inpStr)):
        countConsecutive += 1

        # If next character is different than current, append this char to result.
        if i + 1 >= len(inpStr) or inpStr[i] != inpStr[i + 1]:
            compressedList.append(inpStr[i])
            compressedList.append(str(countConsecutive))
            countConsecutive = 0

    str1 = ""
    if len(compressedList) < len(inpStr):
        return str1.join(compressedList)
    else:
        return inpStr


if __name__ == "__main__":
    inpStr = "aa"
    inpStr = "aabcccccaaa"
    print compress(inpStr)
