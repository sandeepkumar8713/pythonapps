# CTCI : Q17_02_Shuffle
# Question : Write a method to shuffle a deck of cards. It must be a perfect shuffle-in other words, each
# of the 52! permutations of the deck has to be equally likely. Assume that you are given a random
# number generator which is perfect. Given an array of size n, randomly output all the elements one by one.
#
# Question Type : Easy
# Used : Run a loop for n.
#          generate a random number k b/w 0 and n
#          swap card b/w i and k
# Complexity : O(n) n is count of cards

import random


def shuffleArrayIteratively(cards):
    for i in range(len(cards)):
        k = random.randint(0, len(cards) - 1)
        temp = cards[k]
        cards[k] = cards[i]
        cards[i] = temp


if __name__ == "__main__":
    deckSize = 52
    cards = []
    for i in range(deckSize):
        cards.append(i)
    print (cards)
    shuffleArrayIteratively(cards)
    print (cards)
