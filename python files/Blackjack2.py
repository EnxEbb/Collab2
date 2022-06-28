import random

# deck of cards / player dealer hand


class Blackjack:
    def __init__(self, deck, playerHand, dealerHand):
        self.playerHand = playerHand
        self.dealerHand = dealerHand
        self.deck = deck

    # deal the cards

    def dealCard(self, turn, deck):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)
# calculate the total of each hand

    # def __init__(self, card):
    #   self.card = card

    def total(self, turn):
        total = 0
        ace_11s = 0
        face = ['J', 'Q', 'K']
        for card in turn:
            if card in range(11):
                total += card
            elif card in face:
                total += 10
            else:
                total += 11
                ace_11s += 1
        while ace_11s and total > 21:
            total -= 10
            ace_11s -= 1
        return total

# check for winner

    def revealDealerHand(self, dealerHand):
        if len(dealerHand) == 2:
            return dealerHand[0]
        elif len(dealerHand) > 2:
            return dealerHand[0], dealerHand[1]


# game loop

class gulug:
    #playerIn = True
    #dealerIn = True
    #dealerHand = []
    #playerHand = []
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
    #blackie = Blackjack(deck, playerHand, dealerHand)

    def Dealing(self, blackie):
        for _ in range(2):
            blackie.dealCard(blackie.dealerHand, blackie.deck)
            blackie.dealCard(blackie.playerHand, blackie.deck)

    def RUN(self, blackie, playerIn, dealerIn):
        while playerIn or dealerIn:
            print(
                f"Dealer has {blackie.revealDealerHand(blackie.dealerHand)} and X")
            print(
                f"You have {blackie.playerHand}")
            if playerIn:
                stayOrHit = input("1: Stay\n2: Hit\n")
            if blackie.total(blackie.dealerHand) > 16:
                dealerIn = False
            else:
                blackie.dealCard(blackie.dealerHand, blackie.deck)
            if stayOrHit == '1':
                playerIn = False
            else:
                blackie.dealCard(blackie.playerHand, blackie.deck)
            if blackie.total(blackie.playerHand) >= 21:
                break
            elif blackie.total(blackie.dealerHand) >= 21:
                break

        if blackie.total(blackie.playerHand) == 21:
            print(f"\nYou have {blackie.playerHand} for a total of {blackie.total(blackie.playerHand)} and the dealer has {blackie.dealerHand} for a total of {blackie.total(blackie.dealerHand)}")
            print("BlackJack! You win!")
        elif blackie.total(blackie.dealerHand) == 21:
            print(f"\nYou have {blackie.playerHand} for a total of {blackie.total(blackie.playerHand)} and the dealer has {blackie.dealerHand} for a total of {blackie.total(blackie.dealerHand)}")
            print("BlackJack! Dealer wins!")
        elif blackie.total(blackie.playerHand) > 21:
            print(f"\nYou have {blackie.playerHand} for a total of {blackie.total(blackie.playerHand)} and the dealer has {blackie.dealerHand} for a total of {blackie.total(blackie.dealerHand)}")
            print("You bust Dealer wins")
        elif blackie.total(blackie.dealerHand) > 21:
            print(f"\nYou have {blackie.playerHand} for a total of {blackie.total(blackie.playerHand)} and the dealer has {blackie.dealerHand} for a total of {blackie.total(blackie.dealerHand)}")
            print("Dealer busts! You win!")
        elif 21 - blackie.total(blackie.dealerHand) < 21 - blackie.total(blackie.playerHand):
            print(f"\nYou have {blackie.playerHand} for a total of {blackie.total(blackie.playerHand)} and the dealer has {blackie.dealerHand} for a total of {blackie.total(blackie.dealerHand)}")
            print("Dealer wins")
        elif 21 - blackie.total(blackie.dealerHand) > 21 - blackie.total(blackie.playerHand):
            print(f"\nYou have {blackie.playerHand} for a total of {blackie.total(blackie.playerHand)} and the dealer has {blackie.dealerHand} for a total of {blackie.total(blackie.dealerHand)}")
            print("You win")


playerIn = True
dealerIn = True
dealerHand = []
playerHand = []
Start = gulug()
blackie = Blackjack(gulug.deck, playerHand, dealerHand)
Start.Dealing(blackie)
Start.RUN(blackie, playerIn, dealerIn)
