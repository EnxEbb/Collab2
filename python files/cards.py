import random

class Cards(object):
    def __init__(self, suit, val) -> None:
        self.suit = suit
        self.val = val
    
    def show(self):
        print(f"{self.val} of {self.suit}")

class Deck(object):
    def __init__(self) -> None:
        self.card = []
        self.build()
    
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.card.append(Cards(s, v))
    
    def show(self):
        for c in self.card:
            c.show()

    def shuffle(self):
        for i in range(len(self.card) - 1, 0, -1):
            r = random.randint(0, i)
            self.card[i], self.card[r] = self.card[r], self.card[i]
    
    def drawCard(self):
        return self.card.pop()

class Player(object):
    def __init__(self, name):
        name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())  

    def showHand(self):
        for card in self.hand:
            card.show()

