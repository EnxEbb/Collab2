import pygame as p
import numpy as np
import time
from states.state import State

class Life(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.COLOR_BG = (0, 0, 0)
        self.COLOR_GRID = (40, 40, 40)
        self.COLOR_DIE_NEXT = (170, 170, 170)
        self.COLOR_ALIVE_NEXT = (255, 255, 255)
        self.cells = np.zeros((50, 90))
    