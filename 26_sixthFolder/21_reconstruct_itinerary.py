# https://leetcode.com/problems/reconstruct-itinerary/
# Question : You are given a list of airline tickets where tickets[i] = [fromi, toi] represent
# the departure and the arrival airports of one flight. Reconstruct the itinerary in order
# and return it. All of the tickets belong to a man who departs from "JFK", thus,
# the itinerary must begin with "JFK". If there are multiple valid itineraries, you should
# return the itinerary that has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets
# once and only once.
#
# Question Type : ShouldSee
# Used : Make a adjacency map, sort each neighbouring list
#        Now do DFS, starting from 'JFK' and keep appending nodes in ans list.
#        While doing DFS, pop visited nodes and backtrack after dfs.
#        Return True when ans length is equal to ticket count.
#        Our answer is ans list.
#
# Logic: def dfs(u, current_route, current_num_tickets):
#        nonlocal graph, tickets, ans
#        if current_num_tickets == len(tickets):
#           ans = current_route
#           return True
#        for i in range(len(graph[u])):
#           v = graph[u].pop(i)
#           rt = dfs(v, current_route + [v], current_num_tickets + 1)
#           graph[u].insert(i, v)
#           if rt:
#               return True
#        return False
#
#        dfs('JFK', ['JFK'], 0)
#        return ans
# Complexity : O(n)

def findItinerary(tickets):
    graph = dict()

    for u, v in tickets:
        if u in graph.keys():
            graph[u].append(v)
        else:
            graph[u] = [v]

    for u in graph.keys():
        graph[u].sort()

    ans = None

    def dfs(u, current_route, current_num_tickets):

        nonlocal graph, tickets, ans
        if current_num_tickets == len(tickets):
            ans = current_route
            return True

        for i in range(len(graph[u])):
            v = graph[u].pop(i)

            rt = dfs(v, current_route + [v], current_num_tickets + 1)
            graph[u].insert(i, v)
            if rt:
                return True

        return False

    dfs('JFK', ['JFK'], 0)
    return ans


if __name__ == "__main__":
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print(findItinerary(tickets))

    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(findItinerary(tickets))
