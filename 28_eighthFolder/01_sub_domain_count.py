# https://leetcode.com/problems/subdomain-visit-count/
# A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at
# the next level, we have "leetcode.com" and at the lowest level, "discuss.leetcode.com". When we visit a domain
# like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.
# A count-paired domain is a domain that has one of the two formats "rep d1.d2.d3" or "rep d1.d2" where rep
# is the number of visits to the domain and d1.d2.d3 is the domain itself.
# For example, "9001 discuss.leetcode.com" is a count-paired domain that indicates that discuss.leetcode.com
# was visited 9001 times. Given an array of count-paired domains cpdomains, return an array of the count-paired
# domains of each subdomain in the input. You may return the answer in any order.
#
# Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
#
# Question Type : ShouldSee
# Used : Make a dict map. key should be subdomains. key should be visit count
#        We will have to make substrings starting from each dot.
# Logic : for item in cpdomains:
#           substrings = item.split(" ")
#           count = int(substrings[0])
#           sub_domains = substrings[1]
#           updateMap(count_map, sub_domains, count)
#           n = len(sub_domains)
#           for i in range(n):
#               if sub_domains[i] == ".":
#                   updateMap(count_map, sub_domains[i + 1:], count)
#         return count_map
#
#         def updateMap(count_map, sub_domain, count):
#             count_map[sub_domain] = count_map.get(sub_domain, 0) + count
# Complexity : O(n*m)

def updateMap(count_map, sub_domain, count):
    count_map[sub_domain] = count_map.get(sub_domain, 0) + count


def find_domain_count(cpdomains):
    count_map = {}
    for item in cpdomains:
        substrings = item.split(" ")
        count = int(substrings[0])
        sub_domains = substrings[1]
        updateMap(count_map, sub_domains, count)

        n = len(sub_domains)
        for i in range(n):
            if sub_domains[i] == ".":
                updateMap(count_map, sub_domains[i + 1:], count)

    output = []
    for key, value in count_map.items():
        output.append(str(value) + " " + key)

    return output


if __name__ == "__main__":
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(find_domain_count(cpdomains))
