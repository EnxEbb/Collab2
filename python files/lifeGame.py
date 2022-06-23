import pygame as p
import numpy as np

COLOR_BG = (0, 0, 0)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)

class Life:
    def __init__(self) :
        self.COLOR_BG = (0, 0, 0)
        self.COLOR_GRID = (40, 40, 40)
        self.COLOR_DIE_NEXT = (170, 170, 170)
        self.COLOR_ALIVE_NEXT = (255, 255, 255)
    
    def update(self, screen, cells, size, with_progress=False):
        updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

        for row, col in np.ndindex(cells.shape):
            alive = np.sum(cells[row - 1: row + 2, col - 1: col + 2]) - cells[row, col]
            color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

            if cells[row, col] == 1:
                if alive < 2 or alive > 3:
                    if with_progress:
                        color = COLOR_DIE_NEXT
                elif 2 <= alive <= 3:
                    updated_cells[row, col] = 1
                    if with_progress:
                        color = COLOR_ALIVE_NEXT
            else:
                if alive == 3:
                    updated_cells[row, col] = 1
                    if with_progress:
                        color = COLOR_ALIVE_NEXT

            p.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

        return updated_cells