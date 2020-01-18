# CTCI : Q3_05_Sort_Stack
# Question : An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first out" basis.
# People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,or they can select
# whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select
# which specific animal they would like. Create the data structures to maintain this system and implement
# operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linkedlist
# data structure.
#
# Used : Simply use separate queues for dogs and cats, and to place them within a wrapper class called AnimalQueue.
#        We then store some sort of timestamp(or ordernumber) to mark when each animal was enqueued. When we call
#        dequeueAny, we peek at the heads of both the dog and cat queue and return the oldest.
# Complexity : O(n)
#
# TODO :: add code
#
# abstract class Animal {
# private int order;
# protected String name;
# public Animal(String n) {name = n; }
# public void setOrder(int ord) { order
# ord; }
# public int getOrder() { return order; }
# /* Compare orders of animals to return the older item. */
# public boolean isOlderThan(Animal a) {
# return this.order < a.getOrder();
#
# }
# }
