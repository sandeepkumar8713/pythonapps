# https://leetcode.com/discuss/interview-experience/1461079/Google-or-SWE-(L3L4)-or-Dublin-Ireland-or-Reject
# https://github.com/neerazz/FAANG/blob/00fe090a270f0405238e34a14f81e61ec20efd1a/Algorithms/Neeraj/algorithum/design/DesignRestaurant.java
# Question : Build a data structure to perform three operations (Restaurant is full initially):
# 1) waitList (string customer_name, int table_size):
# Add customer with given name and table size they want to book into the waitlist
# 2) leave (string customer_name):
# Customer wants to leave the waitlist so remove them.
# 3) serve (int table_size):
# This means restaurant now has a free table of size equal to table_size. Find the best customer to serve
# from waitlist Best Customer: Customer whose required size is less than or equal to the table_size.
# If multiple customers are matching use first come first serve.
#
# Example : if waitlist has customers with these table requirements => [2, 3, 4, 5, 5, 7] and restaurant is
# serving table_size = 6 then best customer is index 3 (0-based indexing).
#
# Question Type : Generic
# Used : Make a Dict where key : cust name, value : table size
#        Make a Dict where key : table size, value : list of cust name who are waiting
#        waitList() : Insert cust_name and tbl_size in both dict1 and dict2
#        leave(): Remove cust_name from dict1 and dict2 using corresponding tbl_size
#        serve(): Find the key from dict2 which is equal or less than given tbl_size
#                 Now for that key, find the cust list and pop first cust_name
#                 Remove the cust_name from dict1 as well
# Complexity : O(n) where n is no of customer waiting
#               Maybe we can use orderedDict instead of list to reduced retrival time

