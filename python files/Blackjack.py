"""
This is Blackjack by EnxE
"""

from itertools import count
import random

"""
1-13; 14-26; 15-39; 40-52
"""

"""
Cards = ['C_Ace', 'C_2', 'C_3', 'C_4', 'C_5', 'C_6', 'C_7', 'C_8', 'C_9', 'C_10', 'C_Jack', 'C_Queen', 'C_King',
         'D_Ace', 'D_2', 'D_3', 'D_4', 'D_5', 'D_6', 'D_7', 'D_8', 'D_9', 'D_10', 'D_Jack', 'D_Queen', 'D_King',
         'H_Ace', 'H_2', 'H_3', 'H_4', 'H_5', 'H_6', 'H_7', 'H_8', 'H_9', 'H_10', 'H_Jack', 'H_Queen', 'H_King',
         'S_Ace', 'S_2', 'S_3', 'S_4', 'S_5', 'S_6', 'S_7', 'S_8', 'S_9', 'S_10', 'S_Jack', 'S_Queen', 'S_King'
         ]
"""
Cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
         ]

Cards2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
          27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

dealer = []
person = []
DealerCards = []
PersonCards = []


def SHUFFLER(OROLT):
    random.shuffle(OROLT)


def START():
    dealer.append(Cards2[1])
    dealer.append(Cards2[3])
    person.append(Cards2[0])
    person.append(Cards2[2])
    DealerCards.append(Cards[dealer[0] - 1])
    DealerCards.append(Cards[dealer[1] - 1])
    PersonCards.append(Cards[person[0] - 1])
    PersonCards.append(Cards[person[1] - 1])


# def DEAL(Cards, Cards2, dealer, person):

def DEAL():
    if PersonCards.count(1) == 1 and sum(PersonCards) >= 11:
        print("BlackJack")
    # else:

    print(PersonCards)


SHUFFLER(Cards2)
START()
print(Cards2)
print(dealer, person)
print(DealerCards, PersonCards)
