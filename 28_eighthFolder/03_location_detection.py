# Implement a prototype service to detect a user's location based on their IP addresses.
# The IP addresses belonging to the IPv4 space are conventionally represented by four octets, 
# "a.b.c.d". such as 127.10.20.30. To keep it simple, these IP addresses are classified into 5 different regions 
# indexed from 1 to 5 on the basis of the order of the bits in the first octet.
# Broadly, the IP Addresses are categorized as follows:
# 1. 0.0.0.0-127.255.255.255
# 2. 128.0.0.0-191.255.255.255
# 3. 192.0.0.0-223.255.255.255
# 4. 224.0.0.0-239.255.255.255
# 5. 240.0.0.0 255.255.255.255
# Given a list of strings, ip_addresses, of size n, representing possible IPv4 addresses, for each
# address, determine if it is a valid IP or not, and classify it into one of the 5 classes. Return an array of n
# integers that represent the index of the regions for the corresponding IP addresses. Represent an invalid IP as -1.
# 
#  Example: Input :  ip_addresses = ["128.12.34.0", "31.258.90.11"]
#  Output : [2,-1]
# Question Type : Asked


locationMap = [
    (0, 127),
    (128, 191),
    (192, 223),
    (224, 239),
    (240, 255),
]


def isValidIp(ip):
    ipArr = ip.split(".")
    if len(ipArr) != 4:
        return False

    for item in ipArr:
        num = int(item)
        if not (0 <= num <= 255):
            return False

    return True


def find_location(ip_addresses):
    result = []
    for ip in ip_addresses:
        if isValidIp(ip):
            firstSub = int(ip.split(".")[0])
            i = 0
            while i < len(locationMap):
                start, end = locationMap[i]
                if start <= firstSub <= end:
                    result.append(i + 1)
                i += 1
        else:
            result.append(-1)

    return result


if __name__ == "__main__":
    ip_addresses = ["128.12.34.0", "31.258.90.11"]
    print(find_location(ip_addresses))
