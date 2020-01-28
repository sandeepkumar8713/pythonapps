# Question : Given an input stream of boolean values, design a data structure that can support following
# modules in optimal time-
# i) setTrue(index)
# ii) setFalse(index)
# iii) setAllTrue()
# iv) setAllFalse()
# v) getValue(index)
#
# Question Type : Easy
# Used : Make 2 sets, 1 of true and 1 of false.
#        When setTrue and setFalse is called insert index into True or False set
#        When setAllTrue and setAllFalse is called, move the shorter set elements in larger set, and interchange the
#        tag if required
#        getValue() check in both set, else return None
# Complexity : insert O(1), set all O(m) where m is smaller, search O(1)
#
# TODO :: add code


