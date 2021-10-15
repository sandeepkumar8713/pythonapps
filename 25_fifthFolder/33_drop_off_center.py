# https://www.chegg.com/homework-help/questions-and-answers/python-3-autocomplete-ready--1-drop-centers-e-commerce-company-whatdoyou-want-wants-contra-q51225659
# Question : An e-commerce company, WhatDoYou Want, wants to contract with local businesses to
# use their stores as pick- up and drop-off locations for their packages. To reduce expenses,
# they want to ensure that their drop centers are a minimum distance apart from each other.
# A city has many potential drop centers (pdcs) to choose from, represented as nodes on a weighted,
# undirected graph. The edges on this graph denote roads that connect pdcs, with weights
# representing the lengths of the roads. Determine how many unique subsets of these
# companies can be contracted that would satisfy that requirement.
#
# Example :
# Input : graph node = 3, graph_from = [1,2,3], graph_to = [2,3,1], minDist = 4, companies = [1,2,3]
#
# Question Type : Asked
# Used : Make a list of pairs of nodes, whose dist is more than given min distance.
#        Check if the pairs in the nodes can be combined (like 1->2,2->3)
#        keep on combining at each level. (parent, rank)
#        OR count number of possible disjoint set possible in the list.
#        and return subset count of each disjoint set.
#        ans = count of nodes + count of pairs in above list + count of all possible combined nodes
# Complexity : O(m) where m is number of edges
#
# TODO :: add code
#