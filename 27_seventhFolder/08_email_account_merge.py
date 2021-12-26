# https://leetcode.com/problems/accounts-merge/
# Question : Given a list of accounts where each element accounts[i] is a list of strings, where the
# first element accounts[i][0] is a name, and the rest of the elements are emails representing emails
# of the account. Now, we would like to merge these accounts. Two accounts definitely belong to the
# same person if there is some common email to both accounts. Note that even if two accounts have
# the same name, they may belong to different people as people could have the same name. A person
# can have any number of accounts initially, but all of their accounts definitely have the same name.
# After merging the accounts, return the accounts in the following format: the first element of each
# account is the name, and the rest of the elements are emails in sorted order. The accounts
# themselves can be returned in any order.
#
# Example : Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
#          ["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],
#          ["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
#         ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
#
# Question Type : Generic
# Used : Construct our graph, iterating over accounts: for each name: look at emails E1, ..., Ek,
#        then it is enough to connect E1 with each of the others. Perform dfs to find connected
#        components, which we keep as comps with correspondences between number of component
#        and list of emails in this component. We also keep set seen of visited nodes.
#        In the end we just return sort all components and return then.
#        Logic :
#        for acc in accounts:
#           name = acc[0]
#           for email in acc[1:]:
#               graph[acc[1]].add(email)
#               graph[email].add(acc[1])
#               names[email] = name
#        def dfs(node, i):
#           comps[i].append(node)
#           seen.add(node)
#           for neib in graph[node]:
#               if neib not in seen:
#                   dfs(neib, i)
#        for email in graph:
#           if email not in seen:
#               dfs(email, i)
#               i += 1
#        for _, val in comps.items():
#           row = [[names[val[0]]] + sorted(val)]
#           res.append(row)
#        return res
# Complexity : O(a1 log a1 + ... ak * log ak) where ai is the length of accounts[i]

from collections import defaultdict


def accountsMerge(accounts):
    names = {}
    graph = defaultdict(set)

    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            graph[acc[1]].add(email)
            graph[email].add(acc[1])
            names[email] = name

    comps, seen, ans, i = defaultdict(list), set(), [], 0

    def dfs(node, i):
        comps[i].append(node)
        seen.add(node)
        for neib in graph[node]:
            if neib not in seen:
                    dfs(neib, i)

    for email in graph:
        if email not in seen:
            dfs(email, i)
            i += 1

    res = []
    for _, val in comps.items():
        row = [[names[val[0]]] + sorted(val)]
        res.append(row)

    return res


if __name__ == "__main__":
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]

    print(accountsMerge(accounts))
