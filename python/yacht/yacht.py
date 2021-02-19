# """
# This exercise stub and the test suite contain several enumerated constants.

# Since Python 2 does not have the enum module, the idiomatic way to write
# enumerated constants has traditionally been a NAME assigned to an arbitrary,
# but unique value. An integer is traditionally used because it’s memory
# efficient.
# It is a common practice to export both constants and functions that work with
# those constants (ex. the constants in the os, subprocess and re modules).

# You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
# """


# # Score categories.
# # Change the values as you see fit.
# YACHT = None
# ONES = None
# TWOS = None
# THREES = None
# FOURS = None
# FIVES = None
# SIXES = None
# FULL_HOUSE = None
# FOUR_OF_A_KIND = None
# LITTLE_STRAIGHT = None
# BIG_STRAIGHT = None
# CHOICE = None
# DICE = None


# def check_full_houes(dice):
#     dice_set = set(dice)
#     if len(dice_set) == 2:
#         dice_sum = 0
#         for _ in dice:
#             dice_sum += _
#         return dice_sum
#     else:
#         return 0


# def check_four_of_a_kind(dice):
#     dice_set = set(dice)
#     if len(dice_set) == 2:
#         _first, _second = dice_set
#         if dice.count(_first) == 4:
#             return _first * 4
#         elif dice.count(_second) == 4:
#             return _second * 4
#     else:
#         return 0


# def check_choice(dice):
#     dice_sum = 0
#     for _ in dice:
#         dice_sum += _
#     return dice_sum


# def check_yacht(dice):
#     dice_set = set(dice)
#     if len(dice_set) == 1:
#         return 50
#     else:
#         return 0


# def score(dice, category):

#     global DICE
#     DICE = dice

#     print(DICE)

#     global ONES
#     global TWOS
#     global THREES
#     global FOURS
#     global FIVES
#     global SIXES
#     global FULL_HOUSE
#     global FOUR_OF_A_KIND
#     global LITTLE_STRAIGHT
#     global BIG_STRAIGHT
#     global CHOICE
#     global YACHT

#     ONES = dice.count(1) * 1
#     TWOS = dice.count(2) * 2
#     THREES = dice.count(3) * 3
#     FOURS = dice.count(4) * 4
#     FIVES = dice.count(5) * 5
#     SIXES = dice.count(6) * 6
#     FULL_HOUSE = check_full_houes(dice)
#     FOUR_OF_A_KIND = check_four_of_a_kind(dice)
#     dice.sort()
#     LITTLE_STRAIGHT = 30 if dice == [1, 2, 3, 4, 5] else 0
#     BIG_STRAIGHT = 30 if dice == [2, 3, 4, 5, 6] else 0
#     CHOICE = check_choice(dice)
#     YACHT = check_yacht(dice)

#     # if category == ONES:
#     #     return _ONES
#     #     print("ONES  ", dice)
#     # elif category == TWOS:
#     #     return _TWOS
#     #     print("twos  ", dice)
#     # elif category == THREES:
#     #     print("three  ", dice)
#     #     return _THREES

#     # elif category == FOURS:
#     #     print("four  ", dice)
#     #     return _FOURS

#     # elif category == FIVES:
#     #     print("5  ", dice)
#     #     return _FIVES

#     # elif category == SIXES:
#     #     print("6  ", dice)
#     #     return _SIXES

#     # elif category == FULL_HOUSE:
#     #     print("full  ", dice)
#     #     return _FULL_HOUSE

#     # elif category == FOUR_OF_A_KIND:
#     #     print("four kind  ", dice)
#     #     return _FOUR_OF_A_KIND

#     # elif category == LITTLE_STRAIGHT:
#     #     print("ls  ", dice)
#     #     return _LITTLE_STRAIGHT

#     # elif category == BIG_STRAIGHT:
#     #     print("bs  ", dice)
#     #     return _BIG_STRAIGHT

#     # elif category == CHOICE:
#     #     print("cho  ", dice)
#     #     return _CHOICE

#     # elif category == YACHT:
#     #     print("yac  ", dice)
#     #     return _YACHT


from collections import Counter


def full_house(values):
    counter = Counter(values)
    if sorted(dict(counter).values()) == [2, 3]:
        return sum([k * v for k, v in counter.items()])
    return 0


def for_of_a_kind(values):
    counter = Counter(values)
    for k, v in counter.items():
        if v >= 4:
            return k * 4
    return 0


# Score categories
ONES = lambda values: len(list(filter(lambda v: v == 1, values))) * 1
TWOS = lambda values: len(list(filter(lambda v: v == 2, values))) * 2
THREES = lambda values: len(list(filter(lambda v: v == 3, values))) * 3
FOURS = lambda values: len(list(filter(lambda v: v == 4, values))) * 4
FIVES = lambda values: len(list(filter(lambda v: v == 5, values))) * 5
SIXES = lambda values: len(list(filter(lambda v: v == 6, values))) * 6
FULL_HOUSE = full_house
FOUR_OF_A_KIND = for_of_a_kind
LITTLE_STRAIGHT = lambda values: 30 if [1, 2, 3, 4, 5] == values else 0
BIG_STRAIGHT = lambda values: 30 if [2, 3, 4, 5, 6] == values else 0
CHOICE = lambda values: sum(values)
YACHT = lambda values: 50 if len(set(values)) == 1 else 0


def score(dice, category):
    dice.sort()
    return category(dice)