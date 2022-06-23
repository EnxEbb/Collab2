"""
This class handles user input and switches screens if needed.
"""

import pygame as p
from menu import *
import time
import numpy as np
from lifeGame import Life
p.font.init()


class Game():
    def __init__(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = p.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.screen = p.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = "8-BIT WONDER.TTF"
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.COLOR_BG = (0, 0, 0)
        self.COLOR_GRID = (40, 40, 40)
        self.COLOR_DIE_NEXT = (170, 170, 170)
        self.COLOR_ALIVE_NEXT = (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.cells = np.zeros((60, 80))

    def game_loop(self):
        run = False
        while self.playing:
            self.screen.fill(self.COLOR_GRID)
            Life.update(Life, self.screen, self.cells, 10)
            p.display.update()

            if self.playing:
                for event in p.event.get():
                    if event.type == p.QUIT:
                        self.running, self.playing = False, False
                        self.curr_menu.run_display = False
                    elif event.type == p.KEYDOWN:
                        if event.key == p.K_SPACE:
                            run = not run
                            Life.update(Life, self.screen, self.cells, 10)
                            p.display.update()
                    if p.mouse.get_pressed()[0]:
                        pos = p.mouse.get_pos()
                        self.cells[pos[1] // 10, pos[0] // 10] = 1
                        Life.update(Life, self.screen, self.cells, 10)
                        p.display.update()
                self.screen.fill(self.COLOR_GRID)
                if run:
                    self.cells = Life.update(
                        Life, self.screen, self.cells, 10, with_progress=True)
                    p.display.update()
                time.sleep(0.001)
            print(run)


    def check_events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == p.KEYDOWN:
                if event.key == p.K_RETURN:
                    self.START_KEY = True
                if event.key == p.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == p.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == p.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = p.font.SysFont(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
