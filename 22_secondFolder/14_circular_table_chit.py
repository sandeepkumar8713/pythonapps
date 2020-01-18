# Question : A group of people are seated in a circular table. After a while , each members takes a chit and writes his name along
# with the next person name (anticlock wise.)   . If such chits are given , re draw the the table. A optimal approach
# was expected. eg. A - B - C - D - E - A
# chits will be written as A-B
# B-C
# C-D etc
#
# Use a circular linked list, fill it up using the pairs and keep checking. Use a stack to put pairs in it if not found
# in circular list. Pop from stack when something is added in circular list.
#
# Insert first pair in circular queue
# Check if front or rear of the queue is present in next pair
# If present insert in circular queue else in stack
# When something is inserted in queue, front or rear would change. So now search for rear or front in stack, if found
# remove it and add in queue. Repeat until no front or rear is found.
# Go to step 2
#
# Instead  of stack make 2 dict, one for left to right and right to left (easier to search)
#
#  Same questions as above if each member takes a chit and writes his neighbors name . re draw the table.
# Unless input sequence is maintained it is difficult
# TODO :: add code
#
#