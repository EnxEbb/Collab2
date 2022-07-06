import pygame as p
import os

from states.state import State

class game_world(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.background_img = p.image.load(os.path.join("Assets", "space.png"))

    def update(self, dt, action):
        pass
    
    def render(self, display):
        display.blit(self.background_img, (0, 0))

