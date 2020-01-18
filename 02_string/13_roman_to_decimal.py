# Question : Converting Roman Numerals to Decimal lying between 1 to 3999.
# Given a Roman numeral, find its corresponding decimal value.
#
# Used :
# Split the Roman Numeral string into Roman Symbols (character).
# Convert each symbol of Roman Numerals into the value it represents.
# Take symbol one by one from starting from index 0:
#   If current value of symbol is greater than or equal to the value of next symbol,
#       then add this value to the running total.
#   else add the difference between the two to the running total.
# Complexity : O(n)

romanNumMap = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}


def romanToDecimal(romInp):
    result = 0
    i = 0

    while i < len(romInp):
        num1 = romanNumMap[romInp[i]]
        if i+1 <= len(romInp):
            num2 = romanNumMap[romInp[i+1]]
            if num1 >= num2:
                result += num1
                i += 1
            else:
                result += num2 - num1
                i += 2
        else:
            result += num1
            i += 1
    return result


if __name__ == "__main__":
    romInp = "MCMIV"
    print romanToDecimal(romInp)
