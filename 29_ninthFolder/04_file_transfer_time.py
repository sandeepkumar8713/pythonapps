# https://github.com/Zhouzhiling/leetcode/blob/master/Google%20Interview%20Document.docx
# Question : Given a root node, and a filesize of N bytes, calculate the time to transmit the file from
# the root node to the whole network.
#
#                     A
#                  /     \
#               /          \
#  (1500 b/s)  B              C  (1000 b/s)
#            /            /      \
# (400 b/s) D (1000 b/s) E      F (5000 b/s)
#
#
# Question Type : Generic
# Used : Do BFS, steps count will be time spent.
#        Max will be our answer
# Complexity : O(v) where v is no. of nodes.
#
# TODO :: add code
#

