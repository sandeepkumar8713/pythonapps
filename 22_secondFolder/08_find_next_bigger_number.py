# https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
# https://leetcode.com/problems/next-permutation/
# Question : Given a number n, find the smallest number that has same set of digits as n and
# is greater than n. If x is the greatest possible number with its set of digits,
# then print "not possible".
#
# Question Type : Asked
# Used : Convert the given number to list.
#       1) Traverse the given number from rightmost digit, keep traversing till you find a
#          digit which is smaller than the previously traversed digit. For example, if the
#          input number is "534976", we stop at 4 because 4 is smaller than next digit 9.
#          If we do not find such a digit, then output is "Not Possible".
#       2) Now search the right side of above found digit 'd' for the smallest digit greater
#          than 'd'. For "534976", the right side of 4 contains "976". The smallest digit
#          greater than 4 is 6.
#       3) Swap the above found two digits, we get 536974 in above example.
#       4) Now sort all digits from position next to 'd' to the end of number. The number
#          that we get after sorting is the output. For above example, we sort digits
#          in bold 536974. We get "536479" which is the next greater number for input 534976.
#       5) For output convert the list to number
# Complexity : O(m log m)


def findNext(number, n):
    # Start from the right most digit and find the first digit that is smaller than the digit next to it
    for i in range(n - 1, 0, -1):
        if number[i] > number[i - 1]:
            break

    if i == 0:
        print("Next number not possible")
        return

    # Find the smallest digit on the right side of (i-1)'th digit that is greater than number[i-1]
    x = number[i - 1]   # here it is x is 4
    smallest = i
    for j in range(i + 1, n):
        if x < number[j] < number[smallest]:
            smallest = j

    # here smallest number greater than 4 is 6
    # Swapping the above found smallest digit with (i-1)'th
    number[smallest], number[i - 1] = number[i - 1], number[smallest]

    # X is the final number, in integer datatype
    x = 0
    # Converting list upto i-1 into number
    for j in range(i):
        x = x * 10 + number[j]

    # Sort the digits after i-1 in ascending order
    number = sorted(number[i:])
    # converting the remaining sorted digits into number
    for j in range(n - i):
        x = x * 10 + number[j]

    print("Next number with set of digits is", x)


if __name__ == "__main__":
    digits = "534976"
    # converting into integer array, number becomes [5,3,4,9,7,6]
    number = list(map(int, digits))
    findNext(number, len(digits))
