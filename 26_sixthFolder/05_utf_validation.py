# https://leetcode.com/problems/utf-8-validation/
# Question : Given an integer array data representing the data, return whether it is a valid UTF-8 encoding.
# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
# For a 1-byte character, the first bit is a 0, followed by its Unicode code.
# For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes
# with the most significant 2 bits being 10.
#
# Example : Input: data = [197,130,1]
# Output: true
# Explanation: data represents the octet sequence: 11000101 10000010 00000001.
# It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
#
# Question Type : ShouldSee
# Used : Make few variables with few 1 bit set.
#        Like eighth_bit, seventh_bit, sixth_bit, fifth_bit, fourth_bit
#        Loop over the given elements in given data array. Do and operation with above listed vars.
#        trail_count = 0
#        if trail_count > 0:
#           if ele == 10xx_xxxx:
#               trail_count--; continue
#        else:
#           if ele == 0xxx_xxxx: continue
#           else:
#               if ele == 10xx_xxxx: return False
#               if ele == 110x_xxxx: trail_count=1; continue
#               if ele == 1110_xxxx: trail_count=2; continue
#               if ele == 1111_0xxx: trail_count=3; continue
#               return False
#        After the loop if trail_count > 0 return False else True
# Complexity : O(n) n in count of elements in data array


def validUtf8(data):
    eighth_bit = 1 << 7
    seventh_bit = 1 << 6
    sixth_bit = 1 << 5
    fifth_bit = 1 << 4
    fourth_bit = 1 << 3

    trailing_byte_count = 0
    for byte in data:
        if trailing_byte_count > 0:
            if (byte & eighth_bit) and not (byte & seventh_bit):  # 10xx_xxxx
                trailing_byte_count -= 1
                continue
            else:
                return False
        else:
            if not (byte & eighth_bit):  # 0xxx_xxxx
                continue
            else:  # 1xxx_xxxx
                if not (byte & seventh_bit):  # 10xx_xxxx
                    return False
                # 11xx_xxxx
                if not (byte & sixth_bit):  # 110x_xxxx
                    trailing_byte_count = 1
                    continue
                # 111x_xxxx
                if not (byte & fifth_bit):  # 1110_xxxx
                    trailing_byte_count = 2
                    continue
                # 1111_xxxx
                if not (byte & fourth_bit):  # 1111_0xxx
                    trailing_byte_count = 3
                    continue
                return False

    if trailing_byte_count != 0:
        return False

    return True


if __name__ == "__main__":
    data = [197, 130, 1]
    print(validUtf8(data))

    data = [235, 140, 4]
    print(validUtf8(data))
