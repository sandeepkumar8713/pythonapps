# https://leetcode.com/problems/fizz-buzz/
# Question : Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#
# TODO : add used

def fizz_buzz(n):
    result = []
    i = 1
    count = 1
    while i <= 15:
        if count > n:
            break

        if i == 15:
            result.append("FizzBuzz")
            i = 0
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(count))
        i += 1
        count += 1

    return result


if __name__ == "__main__":
    n = 3
    print(fizz_buzz(n))

    n = 5
    print(fizz_buzz(n))

    n = 15
    print(fizz_buzz(n))

    n = 100
    print(fizz_buzz(n))

