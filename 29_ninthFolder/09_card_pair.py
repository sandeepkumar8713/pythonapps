import sys
import re
import functools
from dataclasses import dataclass, field
from typing import List
from collections import defaultdict


@dataclass
class Results:
    set_name: str
    cards: List


#  Example test:   ['2H', '4H', '7C', '9D', '10D', 'KS']
# Output:
# ['2H', '4H', '7C', '9D', '10D', 'KS']
# WRONG ANSWER (Name of card set is detected correctly. Card "JC" does not appear in the input set.)
#
# Example test:   ['AS', '10H', '8H', '10S', '8D']
# Output:
# ['AS', '10H', '8H', '10S', '8D']
# WRONG ANSWER (detected set "single card", but the correct answer is "pair")
#
# Example test:   ['AS', 'JS', 'AH', 'AD', '10D', 'AC']
# Output:
# ['AS', 'JS', 'AH', 'AD', '10D', 'AC']
# WRONG ANSWER (detected set "single card", but the correct answer is "triple")
#
# Example test:   ['6H', '7S', '8S', '9S', '10S', 'JD', 'JC', 'KC', 'AC']
# Output:
# ['6H', '7S', '8S', '9S', '10S', 'JD', 'JC', 'KC', 'AC']
# WRONG ANSWER (detected set "single card", but the correct answer is "five in a row")
#
# Example test:   ['2D', '4D', '6D', '8D', '9D', 'AC', 'KC', 'QC', 'JC', '7C']
# Output:
# ['2D', '4D', '6D', '8D', '9D', 'AC', 'KC', 'QC', 'JC', '7C']
# WRONG ANSWER (detected set "single card", but the correct answer is "suit")
#
# Example test:   ['10D', '10H', '10C', '2S', '2H', '2D', 'JH', 'JC']
# Output:
# ['10D', '10H', '10C', '2S', '2H', '2D', 'JH', 'JC']
# WRONG ANSWER (detected set "single card", but the correct answer is "a triple and a pair")

card_strength = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suit = ['S', 'H', 'D', 'C']


def get_rank_and_suit(card):
    suit = card[-1]
    rank = card[:-1]

    return rank, suit


def find_single_card(cards):
    max_rank = -2
    high_card = None
    for card in cards:
        (rank, suit) = get_rank_and_suit(card)
        # print(rank, suit)
        index = card_strength.index(rank)
        if index > max_rank:
            max_rank = index
            high_card = card

    return high_card


def find_pair_card(cards, num):
    rank_dict = defaultdict(int)
    another_dict = defaultdict(list)
    for card in cards:
        (rank, suit) = get_rank_and_suit(card)
        rank_dict[rank] = rank_dict.get(rank, 0) + 1
        another_dict[rank].append(card)

    max_rank = -2
    high_rank = None
    for rank, value in rank_dict.items():
        if value >= num:
            index = card_strength.index(rank)
            if max_rank < index:
                max_rank = index
                high_rank = rank

    result = another_dict.get(high_rank)
    if result is not None:
        return result[:num]
    return None


def find_five(cards):
    arr = []
    for card in cards:
        (rank, suit) = get_rank_and_suit(card)
        index = card_strength.index(rank)
        arr.append((index, card))

    limit = 5
    result = None
    max_rank = -1
    for i in range(len(arr) - limit):
        sub_arr = arr[i:i + limit]
        count = 0

        for i in range(1, 5):
            if sub_arr[i - 1][0] + 1 == sub_arr[i][0]:
                count += 1

        if count == limit - 1:
            can_result = []
            can_max = -1
            for (index, card) in sub_arr:
                can_result.append(card)
                can_max = max(index, can_max)
            if can_max > max_rank:
                result = can_result

    return result


def find_triple_and_pair(cards):
    triple_high_card = find_pair_card(cards, 3)
    if triple_high_card is not None:
        sub_str = []
        for card in cards:
            if card not in triple_high_card:
                sub_str.append(card)

        if len(sub_str) >= 2:
            pair_high_card = find_pair_card(sub_str, 2)

            if pair_high_card is not None:
                triple_high_card.extend(pair_high_card)
                return triple_high_card

    return None


def solution(cards):
    triple_and_pair = find_triple_and_pair(cards)
    if triple_and_pair is not None:
        return Results(set_name="a triple and a pair", cards=triple_and_pair)

    five_high_card = find_pair_card(cards, 5)
    print
    if five_high_card is not None:
        return Results(set_name="suit", cards=five_high_card)

    five_in_row = find_five(cards)
    if five_in_row is not None:
        return Results(set_name="five in a row", cards=five_in_row)

    triple_high_card = find_pair_card(cards, 3)
    if triple_high_card is not None:
        return Results(set_name="triple", cards=triple_high_card)

    pair_high_card = find_pair_card(cards, 2)
    if pair_high_card is not None:
        return Results(set_name="pair", cards=pair_high_card)

    single_high_card = find_single_card(cards)
    return Results(set_name="single card", cards=[single_high_card])


if __name__ == "__main__":
    # cards = ['2H', '4H', '7C', '9D', '10D', 'KS']
    # print(solution(cards))
    #
    # cards = ['AS', '10H', '8H', '10S', '8D']
    # print(solution(cards))
    #
    # cards = ['AS', 'JS', 'AH', 'AD', '10D', 'AC']
    # print(solution(cards))
    #
    # cards =  ['6H', '7S', '8S', '9S', '10S', 'JD', 'JC', 'KC', 'AC']
    # print(solution(cards))

    cards = ['2D', '4D', '6D', '8D', '9D', 'AC', 'KC', 'QC', 'JC', '7C']
    print (solution(cards))

    # cards = ['10D', '10H', '10C', '2S', '2H', '2D', 'JH', 'JC']
    # print(solution(cards))
