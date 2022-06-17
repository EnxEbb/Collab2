import time
import pygame as p
import numpy as np

class Life():
    def __init__(self):
        p.init()
        self.COLOR_BG = (10, 10, 10)
        self.COLOR_GRID = (40, 40, 40)
        self.COLOR_DIE_NEXT = (170, 170, 170)
        self.COLOR_ALIVE_NEXT = (255, 255, 255)
    
    def update(self, screen, cells, size, with_progress = False):
        updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

        for row, col in np.ndindex(cells.shape):
            alive = np.sum(cells[row - 1: row + 2, col - 1: col + 2]) - cells[row, col]
            color = self.COLOR_BG if cells[row, col] == 0 else self.COLOR_ALIVE_NEXT

            if cells[row, col] == 1:
                if alive < 2 or alive > 3:
                    if with_progress:
                        color = self.COLOR_DIE_NEXT
                elif 2 <= alive <= 3:
                    updated_cells[row, col] = 1
                    if with_progress:
                        color = self.COLOR_ALIVE_NEXT
            else:
                if alive == 3:
                    updated_cells[row, col] = 1
                    if with_progress:
                        color = self.COLOR_ALIVE_NEXT

            p.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

        return updated_cells
    
    def play_game(self):
        screen = p.display.set_mode((800, 600))

        cells = np.zeros((60, 80))
        screen.fill(self.COLOR_GRID)

        p.display.flip()
        p.display.update()

        running = False
        while True:
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    return
                elif event.type == p.KEYDOWN:
                    if event.key == p.K_SPACE:
                        running = not running
                        Life.update(self, screen, cells, 10)
                        p.display.update()
                    if p.mouse.get_pressed()[0]:
                        pos = p.mouse.get_pos()
                        cells[pos[1] // 10, pos[0] // 10] = 1
                        Life.update(self, screen, cells, 10)
                        p.display.update()
            self.screen.fill(self.COLOR_GRID)

            if running:
                self.cells = Life.update(self, screen, cells, 10, with_progress=True)
                p.display.update()
            time.sleep(0.001)


        