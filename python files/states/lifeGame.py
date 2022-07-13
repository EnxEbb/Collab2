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
    
    def get_colors(self):
        return self.COLOR_BG, self.COLOR_DIE_NEXT, self.COLOR_ALIVE_NEXT, self.COLOR_GRID
    
    def update(self, dt, action):
        pass
    
    def update_cell(self, screen, cells, size, progress = False):
        updated_cell = np.zeros((cells.shape[0], cells.shape[1]))
        bg, die_next, alive_next, grid = self.get_colors()

        for row, col in np.ndindex(cells.shape):
            alive = np.sum(cells[row - 1: row + 2, col - 1: col + 2]) - cells[row, col]
            color = bg if cells[row, col] == 0 else alive_next

            if cells[row, col] == 1:
                if alive < 2 or alive > 3:
                    if progress:
                        color = die_next
                elif 2 <= alive <= 3:
                    updated_cell[row, col] = 1
                    if progress:
                        color = alive_next
            else:
                if alive == 3:
                    updated_cell[row, col] = 1
                    if progress:
                        color = alive_next
        p.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

        return updated_cell

    def render(self, display):
        run = False
        display.fill(self.game.COLOR_GRID)
        Life.update_cell(self, self.game.screen, self.cells, 10)
        p.display.update()
        bg, die_next, alive_next, grid = self.get_colors()

        if self.game.playing:
            for event in p.event.get():
                if event.type == p.QUIT:
                    self.game.running, self.game.playing = False
                elif event.type == p.KEYDOWN:
                    if event.key == p.K_SPACE:
                        run = not run
                        Life.update_cell(self, self.game.screen, self.cells, 10)
                        p.display.update()
                if p.mouse.get_pressed()[0]:
                    pos = p.mouse.get_pos()
                    self.cells[pos[1] // 10, pos[0] // 10] = 1
                    p.display.update()
            self.game.screen.fill(grid)
            if run:
                self.cells = Life.update(self.game.screen, self.cells, 10)
                p.display.update()
            time.sleep(0.001)
                


    