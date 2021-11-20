# https://techdevguide.withgoogle.com/resources/compress-decompression/
# https://www.geeksforgeeks.org/decode-string-recursively-encoded-count-followed-substring/
# https://leetcode.com/problems/decode-string/
# Similar : https://leetcode.com/problems/number-of-atoms/
# Question : The question was to decompress the compressed string. I solved it using a stack of strings.
# He then asked me to code my approach on paper so that all corner cases are covered. He then gave
# me 2 or 3 test cases and asked me to dry run my code on these test cases.
#
# Example : Input : "3[b2[ca]]"
# Output : bcacabcacabcaca
#
# Question Type : Generic
# Used : The idea is to use two stacks, one for integers and another for characters.
#        Now, traverse the string,
#           Whenever we encounter any number, push it into the integer stack and in case
#           of any alphabet (a to z) or open bracket ('['), push it onto the character stack.
#           Whenever any close bracket (']') is encountered pop the character from the
#           character stack until open bracket ('[') is not found in the character stack.
#           Also, pop the top element from the integer stack, say n. Now make a string
#           repeating the popped character n number of time. Now, push all character of
#           the string in the stack.
#        Now pop all the elements from string stack. This is the answer.
# Complexity : O(2 * n * m) where n is number of bracket count and m is number of char count


def decode(inpStr):
    integerStack = []
    stringStack = []
    temp = ""
    result = ""

    # Traversing the string
    for i in range(len(inpStr)):
        count = 0
        # If number, convert it into number and push it into integerStack.
        if inpStr[i] >= '0' and inpStr[i] <= '9':
            while inpStr[i] >= '0' and inpStr[i] <= '9':
                count = count * 10 + ord(inpStr[i]) - ord('0')
                i += 1

            i -= 1
            integerStack.append(count)

        # If closing bracket ']', pop elemment until
        # '[' opening bracket is not found in the
        # character stack.
        elif inpStr[i] == ']':
            temp = ""
            count = 0

            if len(integerStack) != 0:
                count = integerStack[-1]
                integerStack.pop()

            while len(stringStack) != 0 and stringStack[-1] != '[':
                temp = stringStack[-1] + temp
                stringStack.pop()

            if len(stringStack) != 0 and stringStack[-1] == '[':
                stringStack.pop()

            # Repeating the popped string 'temp' count number of times.
            for j in range(count):
                result = result + temp

            # Push it in the character stack.
            for j in range(len(result)):
                stringStack.append(result[j])

            result = ""

        # If '[' opening bracket, push it into character stack.
        elif inpStr[i] == '[':
            if inpStr[i - 1] >= '0' and inpStr[i - 1] <= '9':
                stringStack.append(inpStr[i])
            else:
                stringStack.append(inpStr[i])
                integerStack.append(1)

        else:
            stringStack.append(inpStr[i])

        # Pop all the elmenet, make a string and return.
    while len(stringStack) != 0:
        result = stringStack[-1] + result
        stringStack.pop()

    return result


if __name__ == '__main__':
    inpStr = "3[b2[ca]]"
    print(decode(inpStr))

    inpStr = "2[abc]3[cd]ef"
    print(decode(inpStr))

    inpStr = "1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]"
    print(decode(inpStr))
