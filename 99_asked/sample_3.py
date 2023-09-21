# Given an array of int, find second largest.

import heapq


def find_second_largest(nums):
    max_heap = []
    for item in nums:
        heapq.heappush(max_heap, -item)

    largest = -heapq.heappop(max_heap)
    second_largest = -heapq.heappop(max_heap)
    return second_largest


def find_pairs(nums):
    hash_set = set()
    result = []
    for item in nums:
        if (item + 2) in hash_set:
            result.append((item + 2, item))
        if (item - 2) in hash_set:
            result.append((item - 2, item))
        hash_set.add(item)

    return result


import re


def check_if_email_valid(email):
    regexp = re.compile(r'^[a-zA-Z][0-9a-zA-Z_.]*@gmail.com$')
    matched = regexp.search(email)
    if matched:
        return True
    return False


ipconfig = '''lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
en5: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether ac:de:48:00:11:22
	inet6 fe80::aede:48ff:fe00:1122%en5 prefixlen 64 scopeid 0x4
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect (100baseTX <full-duplex>)
	status: active
en1: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 82:4e:37:64:8c:01
	media: autoselect <full-duplex>
	status: inactive
en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 82:4e:37:64:8c:00
	media: autoselect <full-duplex>
	status: inactive
en3: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 82:4e:37:64:8c:05
	media: autoselect <full-duplex>
	status: inactive
en4: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 82:4e:37:64:8c:04
	media: autoselect <full-duplex>
	status: inactive
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether 82:4e:37:64:8c:01
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x0
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 5 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 6 priority 0 path cost 0
	member: en3 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 7 priority 0 path cost 0
	member: en4 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 8 priority 0 path cost 0
	nd6 options=201<PERFORMNUD,DAD>
	media: <unknown type>
	status: inactive
ap1: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether aa:66:5a:56:15:ac
	media: autoselect
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 88:66:5a:56:15:ac
	inet6 fe80::86d:4155:63e:38bc%en0 prefixlen 64 secured scopeid 0xb
	inet 192.168.43.50 netmask 0xffffff00 broadcast 192.168.43.255
	inet6 2409:408a:2c03:bea3:1015:e325:686a:1ea8 prefixlen 64 autoconf secured
	inet6 2409:408a:2c03:bea3:49ca:3911:b13e:c627 prefixlen 64 autoconf temporary
	nat64 prefix 64:ff9b:: prefixlen 96
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
awdl0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6463<RXCSUM,TXCSUM,TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether 0e:6c:a9:e4:99:c2
	inet6 fe80::c6c:a9ff:fee4:99c2%awdl0 prefixlen 64 scopeid 0xc
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
llw0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 0e:6c:a9:e4:99:c2
	inet6 fe80::c6c:a9ff:fee4:99c2%llw0 prefixlen 64 scopeid 0xd
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::8f9b:5eb7:3b59:60c2%utun0 prefixlen 64 scopeid 0xe
	nd6 options=201<PERFORMNUD,DAD>
utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
	inet6 fe80::eec8:c58b:bbf6:6526%utun1 prefixlen 64 scopeid 0xf
	nd6 options=201<PERFORMNUD,DAD>
utun2: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1000
	inet6 fe80::ce81:b1c:bd2c:69e%utun2 prefixlen 64 scopeid 0x10
	nd6 options=201<PERFORMNUD,DAD>'''


def find_ip_addrs(ipconfig):
    regexp = re.compile(r'inet [0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}')
    [] | []
    #regexp = re.compile(r'inet 192.168.43.50')
    eno_found = False
    for line in ipconfig.split("\n"):
        if "en0: " in line:
            eno_found = True
        if eno_found:
            matched = regexp.search(line)
            if matched:
                return matched.group()

    return None

if __name__ == "__main__":
    # nums = [1, 6, 3, 9, 10, 14]
    # print(find_second_largest(nums))

    # print(find_pairs(nums))

    # no int, ., _ 0-9 a-z A-Z
    # email = "sande_ep@gmail.com"
    # print(check_if_email_valid(email))
    #
    # email = "9sanbd@gmail.com"
    # print(check_if_email_valid(email))

    print(find_ip_addrs(ipconfig))

# top elemnent the minimum
# negative value, max heap
# top max value,
# second max value

# space : O(n)
# time : O(n log n)
# dir
#

# select name from user where name like 's%';
# 3 liter 5 liter
# 5 liter, 3 liter
# 2 liter, 3 liter

# 3 liter box, 2 liter
#

# 3 liter -> 5 liter-> 2 liter,
#