# CTCI : Q17_01_Add_Without_Plus
# Question : Write a function that adds two numbers. You should not use+ or any arithmetic
# operators.
#
# Question Type : ShouldSee
# Used : while b != 0:
#         sum = a ^ b  # add without carrying
#         carry = (a & b) << 1  # carry, but don't add
#         a = sum
#         b = carry
#        return a
# Complexity : O(log n)


def add(a, b):
    while b != 0:
        sum = a ^ b  # add without carrying
        carry = (a & b) << 1  # carry, but don't add
        a = sum
        b = carry

    return a


if __name__ == "__main__":
    a = 85
    b = 92
    result = add(a, b)
    print (result)
