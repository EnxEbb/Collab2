import pygame as p
import os
from Blackjack2 import gulug, Blackjack
from states.state import State


class black_runner(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.playerIn = True
        self.dealerIn = True
        self.dealerHand = []
        self.playerHand = []

    def update(self):
        pass

    def render(self):
        Start = gulug()
        blackie = Blackjack(gulug.deck, self.playerHand, self.dealerHand)
        Start.Dealing(blackie)
        Start.RUN(blackie, self.playerIn, self.dealerIn)
