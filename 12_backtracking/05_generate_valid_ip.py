# Question : Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255. The numbers cannot be
# 0 prefixed unless they are 0.
#
# Question Type : Easy
# Used : Run 3 loops from : 0 to n - 2, i + 1 to n - 1 and j + 1 to n.
#        By running these 3 loops split the given string into 4 parts that will give you
#        a ip address. Check if ip is valid, if true then print it.
#        Condition for valid ip: Spilt the ip in 4 parts can check for
#           Sub part should not be of length more than 3. It should be between 0 to 255.
#           It should be more than 0.
#           It should not have 0 as prefix.
# Complexity : O(n^3)


def is_valid(ip):
    ip = ip.split(".")

    # Checking for the corner cases
    for i in ip:
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0':
            return False
    return True


def convert(s):
    sz = len(s)

    if sz < 4:
        return []

    if sz > 12:
        return []
    snew = s
    l = []

    # Generating different combinations.
    for i in range(1, sz - 2):
        for j in range(i + 1, sz - 1):
            for k in range(j + 1, sz):
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]

                # Check for the validity of combination
                if is_valid(snew):
                    l.append(snew)
                snew = s
    return l


if __name__ == "__main__":
    A = "25525511135"
    print(convert(A))

    B = "25505011535"
    print(convert(B))
