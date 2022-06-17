"""
This class is gonna be the class that takes user input and interacts with user. Uses the other engine classes.
"""

import pygame as p

from game import Game
g = Game()

while g.running:
    g.playing = True
    g.game_loop()













# IDLE_WIDTH = IDLE_HEIGHT = 512
# FPS = 60
# BACKGROUND = (255, 255, 255)


# def draw_idle_screen(screen):
#     screen.fill(BACKGROUND)
#     p.display.update()


# def main():

#     p.init()
#     clock = p.time.Clock()
#     screen = p.display.set_mode((IDLE_WIDTH, IDLE_HEIGHT))
#     run = True
#     p.display.update()

#     while run:
#         for event in p.event.get():
#             if event.type == p.QUIT:
#                 run = False

#             if event.type == p.KEYDOWN:
#                 if event.type == p.K_r:
#                     m()
#                     p.display.update()
#             draw_idle_screen(screen)
#         p.display.update()


# if __name__ == "__main__":
#     main()
