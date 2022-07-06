from states.state import State
from states.game_world import game_world
import pygame as p
import os

class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
        # Set the menu 
        self.mid_w, self.mid_h = self.game.GAME_W // 2, self.game.GAME_H // 2
        self.run_display = True
        # Set the cursor and menu states
        self.menu_options = {0: 'game1', 1: 'game2', 2: 'game3'}
        self.index = 0
        self.cursor_img = p.image.load(os.path.join('Assets', 'cursor.png'))
        self.cursor_rect = self.cursor_img.get_rect()
        self.cursor_pos_y = self.mid_h - 33
        self.cursor_rect.x, self.cursor_rect.y = self.mid_w - 35, self.cursor_pos_y

    def update(self, dt, action):
        self.update_cursor(action)
        if action['start']:
            new_state = game_world(self.game)
            new_state.enter_state()
        if action['action2']:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((0, 0, 0))
        # self.game.draw_text(display, "Game states demo.", (255, 255, 255),
        #                     self.game.GAME_W // 2, self.game.GAME_H // 2)
        self.game.draw_text(display, 'game1', (255, 255, 255), self.mid_w, self.mid_h - 31)
        self.game.draw_text(display, 'game2', (255, 255, 255), self.mid_w, self.mid_h)
        self.game.draw_text(display, 'game3', (255, 255, 255), self.mid_w, self.mid_h + 31)
        display.blit(self.cursor_img, self.cursor_rect)

        

    def update_cursor(self, action):
        if action['down']:
            self.index = (self.index + 1) % len(self.menu_options)
        elif action['up']:
            self.index = (self.index - 1) % len(self.menu_options)
        self.cursor_rect.y = self.cursor_pos_y + (self.index * 32)
