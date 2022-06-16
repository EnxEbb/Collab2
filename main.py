"""
This class is gonna be the class that takes user input and interacts with user. Uses the other engine classes.
"""

import pygame as p

# import agme
# import analogue_clock
# from agme import SPACE_WINDOW_WIDTH, SPACE_WINDOW_HEIGHT

IDLE_WIDTH = IDLE_HEIGHT = 512
FPS = 60
BACKGROUND = (0, 0, 0)


def draw_idle_screen(screen):
    # screen.fill(BACKGROUND)
    p.display.update()


def main():

    p.init()
    clock = p.time.Clock()
    screen = p.display.set_mode((IDLE_WIDTH, IDLE_HEIGHT))
    run = True
    p.display.update()

    while run:
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            draw_idle_screen(screen)
        p.display.update()


if __name__ == "__main__":
    main()
