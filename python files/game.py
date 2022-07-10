"""
This class handles user input and switches screens if needed.
"""

import pygame as p
import numpy as np
import time
import os

from states.title import Title


class Game():
    def __init__(self):
        p.init()
        self.GAME_W, self.GAME_H = 480, 270
        self.SCREEN_W, self.SCREEN_H = 900, 500
        self.COLOR_BG = (0, 0, 0)
        self.COLOR_GRID = (40, 40, 40)
        self.COLOR_DIE_NEXT = (170, 170, 170)
        self.COLOR_ALIVE_NEXT = (255, 255, 255)
        self.display = p.Surface((self.GAME_W, self.GAME_H))
        self.screen = p.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.running, self.playing = True, True
        self.action = {'left': False, 'right': False, 'up': False, 'down': False, 'action': False, 'action2': False, 'start': False}
        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.font = p.font.SysFont("lucidasans", 15)
        self.load_states()
        self.cells = np.zeros((50, 90))

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                self.running, self.playing = False, False
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    self.playing, self.running = False, False
                if event.key == p.K_a:
                    self.action['left'] = True
                if event.key == p.K_d:
                    self.action['right'] = True
                if event.key == p.K_w:
                    self.action['up'] = True
                if event.key == p.K_s:
                    self.action['down'] = True
                if event.key == p.K_p:
                    self.action['action'] = True
                if event.key == p.K_o:
                    self.action['action2'] = True
                if event.key == p.K_RETURN:
                    self.action['start'] = True
            if event.type == p.KEYUP:
                if event.key == p.K_a:
                    self.action['left'] = False
                if event.key == p.K_d:
                    self.action['right'] = False
                if event.key == p.K_w:
                    self.action['up'] = False
                if event.key == p.K_s:
                    self.action['down'] = False
                if event.key == p.K_p:
                    self.action['action'] = False
                if event.key == p.K_o:
                    self.action['action2'] = False
                if event.key == p.K_RETURN:
                    self.action['start'] = False
        
    def update(self):
        self.state_stack[-1].update(self.dt, self.action)
    
    def render(self):
        self.state_stack[-1].render(self.display)
        self.screen.blit(p.transform.scale(self.display, (self.SCREEN_W, self.SCREEN_H)), (0, 0))
        p.display.flip()
    
    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now
    
    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def reset_keys(self):
        for action in self.action:
            self.action[action] = False
        
    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)
     
