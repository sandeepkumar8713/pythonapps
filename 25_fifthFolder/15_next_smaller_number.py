# https://www.geeksforgeeks.org/lexicographically-previous-permutation-in-c/
# 22_secondFolder/08_find_next_bigger_number
# Question : Given a word, find lexicographically smaller permutation of it. For example, lexicographically
# smaller permutation of “4321” is “4312” and next smaller permutation of “4312” is “4231”. If the string is
# sorted in ascending order, the next lexicographically smaller permutation does not exist.
#
# Question Type : ShouldSee, SimilarAdded
# Used : 1) Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than
#        the previously traversed digit. For example, if the input number is "43215", we stop at 1(index i)
#        because 1 is smaller than next digit 5. If we do not find such a digit, then output is "Not Possible".
#        2) Find rightmost element's index that is less than str[i - 1]. Now search the right side of i-1,
#        such that element is larger than str[i-1]. For "43215", the right side of 2 contains "15". 1 is smaller than 2.
#        3) Swap the above found two digits, we get 43125 in above example.
#        4) Now reverse all digits from position i to the end of number. The number that we get after reversing is
#        the output. We get "43152" which is the next smaller number than 43215.
#        prevPermutation(inpArr):
#        n = len(inpArr), i = n - 1
#        while i > 0 and inpArr[i - 1] <= inpArr[i]:
#           i -= 1
#        if i <= 0: return False
#        j = n - 1
#        while j > i-1 and inpArr[j] >= inpArr[i - 1]:
#           j -= 1
#        inpArr[i - 1], inpArr[j] = inpArr[j], inpArr[i - 1]
#        subArray = inpArr[i:]
#        resStr = inpArr[:i] + subArray[::-1]
#        return True, resStr
# Complexity : O(n)


def prevPermutation(inpArr):
    n = len(inpArr)
    i = n - 1
    while i > 0 and inpArr[i - 1] <= inpArr[i]:
        i -= 1

    # if string is sorted in ascending order we're at the last permutation
    if i <= 0:
        return False

    # Note - str[i..n] is sorted in ascending order
    # Find rightmost element's index that is less than str[i - 1]
    j = n - 1
    while j > i-1 and inpArr[j] >= inpArr[i - 1]:
        j -= 1

    # Swap character at i-1 with j
    inpArr[i - 1], inpArr[j] = inpArr[j], inpArr[i - 1]

    # Reverse the substring [i..n]
    subArray = inpArr[i:]
    resStr = inpArr[:i] + subArray[::-1]

    x = 0
    # converting the digits into number
    for i in range(n):
        x = x * 10 + resStr[i]

    return True, x


# Driver code
if __name__ == '__main__':
    str = "43215"
    number = list(map(int, str))
    b, str = prevPermutation(number)
    if b:
        print("Previous permutation is", str)
    else:
        print("Previous permutation doesn't exist")
